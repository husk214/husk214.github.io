Kudo EMNLP'18 SentencePiece: A simple and language independent subword tokenizer and detokenizer for Neural Text Processing
==============================================================================================================================

著者

- Taku Kudo (Google)
- John Richardson (Google)

SentencePiece概要
---------------------

- Pre-segmentationされていない文章に Subword Algorithm を実行できるライブラリ

  - Subword Algorithm: BPE or Unigram model
  - C++実装, python wrapperあり, tensorflow-textにも統合されている

- EMNLPの論文自体はライブラリの実装の話がメインで、アルゴリズムの話はされていない
- 著者によるQiita https://qiita.com/taku910/items/7e52f1e58d0ea6e7859c

Subword
--------

- 高頻度語はそのまま分割、低頻度語は文字や部分文字列に分割するような感じ

  - 例えば、「annoyingly」が低頻度語なので、「annoying」と「ly」に分割する感じ

- モチベーション: 単語による分割では、分割数多すぎてつらい

  - NMT(機械翻訳)では、語彙数が多いとRNNを用いたテキスト生成の計算コストが高く、高頻度語のみに限定すると低頻度が捨てられてしまう

- 最近のTransformerを使った事前学習済みモデルは、Subwordアルゴリズムによってtokenizeされている

  - BERTでよく見る語彙数は32,000とか (少なぎでは? と思っていたけどSubwordはこんなもんらしい)
  - HuggingFaceの `Summary of the tokenizers <https://huggingface.co/transformers/tokenizer_summary.html>`_ にその辺書いてあるが

    - ALBERT, XLNet, Marian, T5ではSentencePiece(Unigram)を使っている
    - BERT, DistilBERT, Electraで使われているは WordPiece (BPEと似たような感じ)

Subword Algorithm
--------------------
Byte-Pair Encoding (BPE) [Sennrich16]_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- unigramとは逆で、文字集合から始まって、greedyにsubwordを追加していく感じ
- https://www.slideshare.net/ssuserd79a5c1/2019bpe がわかりやすい

Unigram model [Kudo18]_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- 概要: 十分に大きい語彙からスタートして、ULMの尤度の減少が最小となるように語彙を除去していく感じ
- モチベーション:

  - BPE, WordPieceは決定的なアルゴリズムで、複数の分割を出力するのは困難で、確率的に扱えないのでn-bestな出力もできない
  - 言語モデルに基づいていない

Unigram model: 文章Xの任意の分割 :math:`\mathbb{x} := \{x_1, \ldots, x_M\}` の分割確率 :math:`P(\mathbb{x})` を各サブワードの生起確率 :math:`p(x_i)` の積 で表す (eq. :eq:`unigram` )

.. math:: P(\mathbb{x}) =  \prod_{i=1}^M p(x_i), ~~ \forall i ~~ x_i \in \mathcal{V}, ~~ \sum_{x \in \mathcal{V}} p(x) = 1
   :label: unigram

**Training Algorithm**

- Input: training corpus (:math:`D: = \{X^{(s)}\}_{s=1}^{|D|}`), 語彙数

  - S(X): 文章Xの全分割候補集合 (語彙集合は与えられる)

- 十分に大きなサイズの語彙集合 :math:`\mathcal{V}` を作る

  - 例えば、全文字集合 + Suffix array algorithmでtraining corpusの上位100万語の高頻度部分文字列を列挙する

- :math:`\mathcal{V}` が設定された語彙数になるまで、以下を繰り返す

  - :math:`p(x_i)` をそれを隠れ変数とする尤度L (eq :eq:`likelihood` ) をEMアルゴリズムによって最大化することで推定する

    - The most probable segmentaion :math:`\mathbb{x}^* = \arg \max_{\mathbb{x} \in S(X)} P(\mathbb{x})` は Viterbiアルゴリズムによって計算可能

  - :math:`x_i \in \mathcal{V}` に対して :math:`x_i` を削除したときの尤度Lの損失(貢献度)を計算

  - 貢献度の小さい :math:`\eta` % (e.g., 20%) の語彙を :math:`\mathcal{V}` から削除 (ただし、1文字が1語彙となるものは残す)

.. math:: L = \sum_{s=1}^{|D|} \log P(X^{(s)}) = \sum_{s=1}^{|D|} \log \left( \sum_{\mathbb{x} \in S(X^{(s)})} P(\mathbb{x}) \right)
   :label: likelihood



参考文献
---------

.. [Sennrich16] Rico Sennrich, Barry Haddow, Alexandra Birch. Neural Machine Translation of Rare Words with Subword Units. In ACL 2016.

.. [Kudo18] Taku Kudo. Subword Regularization: Improving Neural Network Translation Models with Multiple Subword Candidates. In ACL 2018.
