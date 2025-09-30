Roth CVPR'22 Integrating Language Guidance into Vision-based Deep Metric Learning
=============================================================================================

- 著者 : Karsten Roth (1), Oriol Vinyals (2), Zeynep Akata (1,3)

  - 1: University of Tubingen, 2: DeepMind, 3: MPI for Intelligent Systems

- https://arxiv.org/pdf/2203.08543

Abstract 
-------------

(NotebookLMさんに要約してもらいました)

- この論文では、視覚的類似学習モデルの汎化能力を向上させるために、言語ガイダンスという新しいアプローチを提案しています。
- DML（Deep Metric Learning）は、意味的な類似性を埋め込み空間距離として符号化するメトリック空間を学習することを提案しています。 
- しかし、従来のDML手法の多くは、クラスラベルのみに基づいてランキングタスクを定義しており、クラス間の高レベルの意味関係を考慮に入れていません。

- この問題に対処するために、この論文では、事前トレーニング済みの大規模言語モデルを活用してクラスラベルにタスクに依存しない文脈を与え、DMLモデルがより意味的に一貫性のある視覚的表現空間を学習できるようにすることを提案しています。

- 具体的には、2つの言語ガイダンスの方法が提案されています。

  - 専門家言語ガイダンス（ELG）: 専門家が作成したクラスラベル名を利用して、事前トレーニング済みの言語モデルを用いて言語埋め込みとそれぞれの言語的類似性を計算します。そして、これらの言語的類似性を蒸留によって用いることで、標準的なDML手法によって学習された視覚的埋め込み関係を再配置及び修正します。

  - 疑似ラベル言語ガイダンス（PLG）: 専門家によるラベル付けを必要とせず、DMLパイプラインで広く使用されているImageNet事前トレーニングを活用します。 事前トレーニング済みのバックボーンと分類器ヘッドを用いて、各サンプルに対してImageNetのすべてのクラスに対応するソフトマックス出力を生成し、クラスごとに平均化した後、上位k個のImageNet疑似クラス名をそのクラスの表現として選択します。 これらの疑似ラベルを事前トレーニング済みの言語モデルに再埋め込みすることで、より粗いながらも広く適用可能な疑似ラベルの類似性のコレクションにアクセスでき、それを言語ガイダンスに利用できます。

- 広範な実験とアブレーションにより、提案されたアプローチの妥当性が裏付けられ、追加の視覚的な意味的改良のために事前トレーニング済みの言語モデルを使用した場合に、DMLモデルの汎化性能が大幅に向上することが示されています。 
- その結果、トレーニング時間にほとんどオーバーヘッドをかけることなく、すべての標準的なベンチマークにおいて競争力のある最先端の性能を達成することができました。


提案手法
----------

- 手続き的にはシンプルで普通のDMLの損失に画像の方の類似度行列と画像のテキストを言語モデルに通して出ていたベクトル同士の類似度行列のKL距離を加えるだけ。
- 提案法は2種類ある、画像のテキストをどうやって用意するかの違い。

.. image:: ../img/ml/lang_fig2.png
  :scale: 80%
  :align: center


Language Guidance with Expert Class Names (ELG)
"""""""""""""""""""""""""""""""""""""""""""""""""

- 画像のクラス名が使える状況を考える

.. math::
  :nowrap:

  \begin{align}
    \mathcal{L}_{ELG} &= \mathcal{L}_{DML} + \omega \cdot \mathcal{L}_{match}, ~~~ (\omega \text{は係数}) 
  \end{align}

:math:`\mathcal{L}_{DML}` が普通のDMLのロスで :math:`\mathcal{L}_{match}` が画像の方の類似度行列と画像のテキストを言語モデルに通して出ていたベクトル同士の類似度行列のKL距離

.. math::
  :nowrap:

  \begin{align}
    \mathcal{L}_{match} (S^{img}, S^{lang}) &= \cfrac{1}{|B|} \sum_{i}^{|B|} \sigma(S^{img, X}_i) \cdot \log \left( \cfrac{\sigma(S^{img, X}_i)}{\sigma(S^{lang}_i + \gamma_{lang}) } \right)
  \end{align}


- :math:`\sigma` はsoftmaxで、 :math:`\gamma_{lang}` は計算を安定化させるためのもの的ななにか
- :math:`S^{lang}_i` は 「a photo of :math:`y_i` 」 (:math:`y_i` は画像のクラス名) をという文字列を言語モデル(BERTやRoBERTa)に入れてベクトル化してミニバッチ内の組み合わせで類似度を計算した類似度行列
- :math:`S^{img, X}_{i,j} = \mathbb{I}_{y_i = y_j} [1 + \gamma_{lang}] + \mathbb{I}_{y_i \neq y_j}[S^{img}_{i, j}]` で (:math:`y_i = y_j` のときは1, :math:`y_i \neq y_j` のときは画像の類似度行列としたもの )

  - :math:`y_i = y_j` のときは langのほうは常に1だが、imgのほうは(まったく同じ画像でなければ)1より小さい. そのため蒸留中にクラス内の分解能を失わないためにこのような処理をしているとのこと。

    - (同クラスのときは無理にlangのほうに合わせにいかないほうがいいってことだと思うが、これがクリティカルなのかどうかは気になる)


- 言語側はパラメータ更新しない


Language Guidance without extra supervision (PLG)
""""""""""""""""""""""""""""""""""""""""""""""""""""

- pretrainされた画像モデルのアウトプットを使って画像分類してクラス名をを用意する。
- 教師ラベルを言語モデルに入れたembeddingを、ImageNetで学習したモデルの分類結果TopKのクラス名を言語モデルに入れたembedingの平均で大体する。

.. math::
  :nowrap:

  \begin{align}
    \mathcal{L}_{PLG} &= \mathcal{L}_{DML} + \omega \cdot \mathcal{L}^k_{pseudomatch}, ~~~ (\omega \text{は係数}) \\
    \mathcal{L}^k_{psedumatch} &= \mathcal{L}_{match} \left( S^{img}, \frac{1}{k} \sum_{j}^{k} S^{pseudolang, j} \right)
  \end{align}

- :math:`\{ S^{pseudolang, j} \}_{j \in [k]}` はImageNetで学習したモデルの分類結果TopKのクラス名を言語モデルに入れたembeding


実験
----------

モデル

- 画像側のpretrained modelはいろいろなモデルを試して実験する
- 言語側のモデルもいろいろ試すが、基本的にはCLIPの言語側のtransformerを使う

実験手順　(Metric Learning論文あるあるのやつ)

- 学習: クラスラベルがついたデータセットをtrain, testに分割(testにあるクラスはtrainは含まれない)し、trainで学習
- 評価:

  - testデータでクエリ画像を選ぶ
  - 残りの画像に対して類似度を計算して検索
  - 同じクラスの画像がTop (k)にあるか (Recall@1, mAP @ 100)

評価指標

- Recall@1: Top 1に同じクラスの画像を持ってこれている率 (これをP@1と言っている論文もあるが)
- mAP @100: Top 100に同じクラスの画像を持ってこれている数 / 100の平均をクラスごとに平均をとる
- NMI (Normalized Mutual Information): クラスタリングの性能を測る指標 (どれだけうまく埋め込めているか)

  - 具体的な計算手順: https://course.ccs.neu.edu/cs6140sp15/7_locality_cluster/Assignment-6/NMI.pdf 


データセット (Metric Learning論文あるあるのやつ)

- CUB200-2011 (Wah, Catherine, et al. "The caltech-ucsd birds-200-2011 dataset." (2011).)

  - 200種類の鳥の画像 (11,788枚)　
  - 今回使われていないが、クラス名だけではなく部位のバウンディングボックスや位置などもアノテーションされている


.. image:: ../img/ml/cub200_fig1.png
  :scale: 80%
  :align: center


- CARS196 (Krause, Jonathan, et al. "3d object representations for fine-grained categorization." 2013.)

  - 196種類の車の画像 (16,815枚)
  - https://www.tensorflow.org/datasets/catalog/cars196

.. image:: ../img/ml/cars196_fig1.png
  :scale: 80%
  :align: center

- SOP (Stanford Online　Products) (Oh Song, Hyun, et al. "Deep metric learning via lifted structured feature embedding." 2016.)

  -  22,634クラスの商品画像 (120,053枚)


.. image:: ../img/ml/sop_fig1.png
  :scale: 80%
  :align: center


提案手法の効果
"""""""""""""""""""""""""""""""""""""""""""""""""

- 損失、画像側のモデルを変えて性能を見ている
- CUB200, CARS196では精度上がっているが、SOPではほとんど効果がない

  - SOPはクラス数が多い、それに加えてクラス毎のサンプル数が少ない。
  - さらに12個のスーパークラスは名前がついているが、普通のクラスはexpertによるアノテーションがない。
  - そういう状況なので言語を使うというのがうまくいかなかったとのこと。

- CUB200, CARS196は :math:`omega \in [1, 10]` で上手くいとのこと
- だが、SOPは :math:`omega \in [0.1, 1]` とのことなのでうまく効いていないことがわかる

.. image:: ../img/ml/lang_tab1.png
  :scale: 100%
  :align: center


ELGとPLG
"""""""""""""""""""""""""""""""""""""""""""""""""

- どっちもあんまり変わらない

.. image:: ../img/ml/lang_tab2.png
  :scale: 100%
  :align: center

言語モデル
"""""""""""""""""""""""""""""""""""""""""""""""""

- CLIPでなくてもうまくいく
- なんならFastText等のword embeddingでも結構上がる

.. image:: ../img/ml/lang_tab3.png
  :scale: 100%
  :align: center

