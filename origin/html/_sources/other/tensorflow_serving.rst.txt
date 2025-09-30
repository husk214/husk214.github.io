Tensorflow Serving
=====================

Tensorflow Serving (TFS)のすごいと思う所
---------------------------------------------

- はやい & 沢山食える

  - 軽いモデルなら数millisecで返ってくる

- 前後処理をモデルに組み込み可能

  - 前処理、後処理をモデルに追加することでTFSにやってもらい、前段処理のためのgateway server的なものを省略できるケースがある
  - 前処理の例: 文字列を正規化→tokenize→token ID列に変換
  - 後処理の例: 分類モデルだとして、最大の確率になるクラスの名前を返す

- モデルのWarmup

  - モデルの初回実行は時間がかかるが、warmup fileを作成しておけば起動時/読み込み時にwarmupしてくれる

- モデル自動読み込み

  - 新しいversionのモデルを置いたら、自動で読み込んでくれる


はやい & 沢山食える
^^^^^^^^^^^^^^^^^^^^^^^

- 例えば、以下のLSTM+Transfomerみたいなモデル(embedding_dim=256, n_layer=1) だと入力が検索クエリだったら

  - レイテンシー: 平均 3ms, 99%tile 5ms
  - 1vCPU, 1G Memで150QPS食える

.. code-block:: python

  model = AttentionLstms(vocab_size=30000, embedding_dim=256, n_layer=1)

  class AttentionLstms(tf.keras.Model):
      def __init__(self, vocab_size, embedding_dim, n_heads, n_layer=1):
          super().__init__()
          self.sqrt_embedding_dim = tf.math.sqrt(tf.cast(embedding_dim, tf.float32))
          self.embedding = keras.layers.Embedding(vocab_size, embedding_dim, mask_zero=True)
          self.enc_layers = tf.keras.Sequential([AttentionLstmEncoderLayer(embedding_dim, n_heads)  for _ in range(n_layer)])
      @tf.function
      def call(self, inputs, training=False):
          x = self.embedding(inputs, training=training)
          x *= self.sqrt_embedding_dim
          x = self.enc_layers(x, training=training)
          return tf.nn.l2_normalize(x[:, -1, :], -1)

  class AttentionLstmEncoderLayer(tf.keras.Model):
      def __init__(self, embedding_dim, n_heads, bidirectional_lstm=False):
          super().__init__()
          if not bidirectional_lstm:
              self.lstm = tf.keras.layers.LSTM(embedding_dim, return_sequences=True)
          else:
              self.lstm = tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(embedding_dim, return_sequences=True))
              embedding_dim *= 2
          self.mha = MultiHeadAttention(embedding_dim, n_heads)
          self.layernorm1 = tf.keras.layers.LayerNormalization(epsilon=1e-6)
          self.layernorm2 = tf.keras.layers.LayerNormalization(epsilon=1e-6)
          self.ffn = point_wise_feed_forward_network(embedding_dim, 2 * embedding_dim)
      @tf.function
      def call(self, inputs, training=False):
          x = self.lstm(inputs, training=training)
          attn_output, _ = self.mha(x, x, x)
          out1 = self.layernorm1(x + attn_output)
          ffn_output = self.ffn(out1)
          out2 = self.layernorm2(out1 + ffn_output)
          return out2


前後処理をモデルに組み込み可能
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- 例えば、名前と住所の文字列を辞書的に渡して、分散ベクトル返してもらう例 (tf & tf-text==2.3.0)

  - 行っている前処理

    - NGワード処理等の前処理

      - `tensorflow-text <https://github.com/tensorflow/text#normalization>`_ にもいろいろNLPの前処理が実装されている (NFKC正規化とかいろいろ)

    - SentencePiece ( :doc:`sentencepiece` ) によってtokenizeして、token id列化 (よくわからないが、2.3.0以上でないとsave時にエラーで落ちる)
    - nameとaddressを連結


こんな感じで叩ける

.. code-block::

  > curl -d '{"instances": [{"name": "品川プリンスホテル", "address": "東京都港区高輪4-10-30"}]}' -X POST [TFSのURL]
  {
    "predictions": [[-0.00571914762, 0.097049661, -0.0528469719, -0.0421413593, ...]]
  }

上の処理をするモデルをTFSがservingできる形式(SavedModel)で保存するpythonコード

.. code-block:: python

  model = AttentionLstms(vocab_size=30000, embedding_dim=256, n_layer=1)
  model.load_weights("学習済みのモデルをsave_weightsしたファイルパス")
  spm_model_path = "sentencepieceの学習済みモデルのファイルパス"
  encoder = TextVectorizationEncoder(model, spm_model_path, max_sequence_length=15)

  x_n = tf.constant(["品川プリンスホテル"])
  x_a = tf.constant(["東京都港区高輪4-10-30"])
  x_s = encoder.preprocess(x_n, x_a)
  outputs_spot = encoder(x_s)
  print(outputs_spot[0, :5])
  """
  出力:
  tf.Tensor(
  [-0.00571914762, 0.097049661, -0.0528469719, -0.0421413593,
   -0.0743320137], shape=(10,), dtype=float32)
  """

  @tf.function(input_signature=[tf.TensorSpec(shape=[None], dtype=tf.string, name="name"), tf.TensorSpec(shape=[None], dtype=tf.string, name="address")])
  def predict_fn_spot(name, address):
      x = encoder.preprocess(name, address)
      output = encdoer(x)
      return {"vector": output}

  signatures_spot = {'serving_default': predict_fn_spot.get_concrete_function()}
  # tfsでservingできる形式で保存する
  tf.saved_model.save(model_spot, "SavedModelの保存先ファイルパス", signatures_spot)

  class Normalizer(keras.layers.Layer):
      # lower変換, NGワード除去等の正規化をする
      def __init__(self, ng_words):
          super(Normalizer, self).__init__()
          ng_words = list(sorted(ng_words, key=len, reverse=True))
          self.ng_word_regexp = "|".join(ng_words)
          self.zenkaku_space = "　"
          self.all_space_regexp = " +"

      def call(self, inputs):
          x = tf.strings.regex_replace(inputs, self.zenkaku_space, " ")
          x = tf.strings.regex_replace(x, self.all_space_regexp, " ")
          x = tf.strings.lower(inputs)
          x = tf_text.normalize_utf8(x)
          x = tf.strings.regex_replace(x, self.ng_word_regexp, "")
          return tf.strings.strip(x)

  class TextVectorizationEncoder(tf.keras.Model):
      # nameとaddressを入力に、前処理した後モデルにいれて、分散ベクトルを返す
      def __init__(
          self, model, tokenizer_path, max_sequence_length, ng_words=[],
      ):
          super().__init__()
          self.max_sequence_length = tf.constant(max_sequence_length, dtype=tf.int64)
          self.normalizer = Normalizer(ng_words)
          self.tokenizer = tf_text.SentencepieceTokenizer(
              model=open(tokenizer_path, "rb").read()
          )
          self.model = model
          self.sep_id = 4
        self.len_address_token = 10
      def left_pad_2d_ragged(self, rt):
          """ https://github.com/tensorflow/tensorflow/issues/34793
          RaggedTensor.to_list()がgraph modelで使えないので、pad_sequences(RaggedTensor.to_list())を使う選択肢は今のところ無い
          """
          rt = rt[:, :self.max_sequence_length]  # Truncate rows to have at most `width` items
          pad_row_lengths = tf.maximum(tf.constant(0, tf.int64), self.max_sequence_length - rt.row_lengths())
          pad_values = tf.zeros([self.max_sequence_length * rt.nrows() - tf.size(rt, tf.int64)], rt.dtype)
          padding = tf.RaggedTensor.from_row_lengths(pad_values, pad_row_lengths)
          return tf.concat([padding, rt], axis=1).to_tensor()
    def preprocess(self, name, address):
        x_n = self.tokenizer.tokenize(self.normalizer(name))
        x_a = self.tokenizer.tokenize(self.normalizer(address))
        sep = tf.RaggedTensor.from_tensor(tf.fill((tf.shape(name)[0] ,1), self.sep_id))
        x = tf.concat((x_a[:, :self.len_address_token], sep, x_n), axis=1)
        return self.left_pad_2d_ragged(x)
      def call(self, x):
          return self.model(x, training=False)

モデルのWarmup
^^^^^^^^^^^^^^^^^

- https://www.tensorflow.org/tfx/serving/saved_model_warmup に書いてある

  - TensorFlowランタイムの一部のコンポーネントはlazy initilizedされる
  - -> モデルがロードされた後の最初のリクエストのレイテンシは桁違いに高い
  - -> SavedModelと一緒にリクエストのサンプルを提供することで、モデルのロード時にサブシステムとコンポーネントの初期化をトリガーできる

- TFSの起動オプションに --enable_model_warmup=true を渡す必要がある

前処理のところの例ででてきたモデルのWarmupクリエスとファイルを作成するコード

.. code-block:: python

  with tf.io.TFRecordWriter(f"SavedModelの保存先ファイルパス/assets.extra/tf_serving_warmup_requests") as writer:
      predict_request = predict_pb2.PredictRequest()
      predict_request.model_spec.name = 'spot_v1'
      predict_request.model_spec.signature_name = 'serving_default'
      predict_request.inputs['name'].CopyFrom(tensor_util.make_tensor_proto(["品川プリンスホテル"], tf.string))
      predict_request.inputs['address'].CopyFrom(tensor_util.make_tensor_proto(["東京都港区高輪四丁目10番30号"], tf.string))
      log = prediction_log_pb2.PredictionLog(predict_log=prediction_log_pb2.PredictLog(request=predict_request))
      for r in range(NUM_RECORDS):
          writer.write(log.SerializeToString())

TFSがwarmupしてくれているログ

.. code-block::

  dev-query-inference-f56ddb897-7gcrn inference 2020-12-14 10:11:16.896762: I tensorflow_serving/servables/tensorflow/saved_model_warmup_util.cc:118] Finished reading warmup data for model. Number of warmup records read: 100. Elapsed time (microseconds): 10247322.
  dev-query-inference-f56ddb897-7gcrn inference 2020-12-14 10:11:17.867244: I tensorflow_serving/core/loader_harness.cc:87] Successfully loaded servable version {name: query version: 6}
  dev-query-inference-f56ddb897-7gcrn inference 2020-12-14 10:11:17.867321: I tensorflow_serving/core/loader_harness.cc:138] Quiescing servable version {name: query version: 1}
  dev-query-inference-f56ddb897-7gcrn inference 2020-12-14 10:11:17.867332: I tensorflow_serving/core/loader_harness.cc:145] Done quiescing servable version {name: query version: 1}

モデル自動読み込み
^^^^^^^^^^^^^^^^^^^^^^^

- 新しいversionのモデルをs3におくと、新しいモデル読み込んでくれる (固定もできる)

  - デフォルトの設定だと、s3にリスト参照リクエストを結構送ってしまうので、--file_system_poll_wait_seconds=300とかに設定しておくとよい

- 新しいversionのモデルを読み込んだら、古いモデルのメモリは開放されるようだった

  - TFSが確保しているメモリは開放されないが、何回でも新しいモデル読み込めそうだった
