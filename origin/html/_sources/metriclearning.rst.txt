==================================
Metric Learning
==================================

***********************
Papers
***********************


.. toctree::
  :maxdepth: 1

  metriclearning/reality_check
  metriclearning/lifted_structured
  metriclearning/multi_similarity
  metriclearning/proxy_nca
  metriclearning/proxy_anchor
  metriclearning/s2sd
  metriclearning/clip
  metriclearning/lang_guide

***********************
Metric Learningとは
***********************

- 一般的に記述できる枠組みはよくわからない

  - ふんわりしすぎている印象 (なんでもMetric Learningと言ってしまえるような感じがする)
  - 応用先によって問題設定が異なるので何とも言えないと思っている

- 雰囲気は、いい感じにデータを変換する関数を学習することをMetric Learningと呼んでいる気がする



応用先
--------

- 顔認証

  - 同一人物の画像どうしの距離を小さく、違う人物どうしの距離を遠くするように関数を学習する

- 情報検索(例えば画像検索)

  - 同じような画像どうしの距離を小さく、違う感じの画像どうしの距離を遠くするように関数を学習する

- 異常検知
- Learning to Rank
- etc...


ロス関数
-----------

- 分類問題のロス(Cross Entropy)から派生したロス(Classification losses)とそうでないもの(Embedding losses)がある by [Musgrave20]_
- [Musgrave20]_ によると、Proxy族は Classification losses になっているが、Embedding lossesだと思う

**Notation**

- :math:`S_{ij} := s(x_{i}, x_{j})`, サンプルiとサンプルjの類似度

  - :math:`x_{i}` : サンプルiのembedding
  - :math:`s(\cdot, \cdot)` : 2つのサンプルの類似度を測る関数 (例: 内積, cosine類似度)

- :math:`[x]_+ := \max(x, 0)`

Embedding losses
^^^^^^^^^^^^^^^^^^^

- **Contrastive loss** [Hadsel06]_ - 同じラベルなら類似度が高く、違うラベルなら低くなるように学習する

  - :math:`I_{ij} := 1 ~~\text{if}~~ y_i = y_j ~~\text{else}~~ 0`
  - :math:`y_i` : サンプルiのラベル
  - :math:`m_p, m_n` : positive pairのマージン(例: 1.0), negative pairのマージン (例: 0.5)

.. math::
  :nowrap:

  \begin{align}
    L_{constract}(x_i, x_j) := I_{ij} [m_p - s(x_i, x_j) ]_+ + (1-I_{ij}) [s(x_i, x_j) - m_n]_+
  \end{align}

- **Triplet loss** [Hoffer15]_ - aとpの類似度より、aとnの類似度が低くなるように学習する

  - :math:`a, n, p` : a=anchorサンプル, n=aのnegative pair, p=aのpositive pair

.. math::
  :nowrap:

  \begin{align}
    L_{triplet}(x_a, x_p, x_n) := [s(x_a, x_n) - s(x_a, x_p) + m ]_+
  \end{align}


- **N-pair loss** [Sohn16]_ - N-pairに拡張したもの

.. math::
  :nowrap:

  \begin{align}
    L_{N-pair-mc} (\{x_i, x^+_i\}_{i=1}^N) &:= \cfrac{1}{N} \sum_{i=1}^{N}
      \log \left(1 + \sum_{j \neq i } \exp(s(x_i, x_j^+) - s(x_i, x^+_i) ) \right) \\
    L_{N-pair-ovo} (\{x_i, x^+_i\}_{i=1}^N) &:= \cfrac{1}{N} \sum_{i=1}^{N}
      \sum_{j \neq i } \log \left(1 + \exp (s(x_i, x_j^+) - s(x_i, x^+_i) ) \right)
  \end{align}

- **Lifted Structure loss** [Song16]_ :doc:`metriclearning/lifted_structured`

  - :math:`\mathcal{X}` : ミニバッチ (embeddingの集合)
  - :math:`\mathcal{X}^+_{x_i}` : ミニバッチ内の :math:`x_i` と同じクラスのembeddingの集合
  - :math:`\mathcal{X}^-_p` : ミニバッチ内の :math:`x_i` とは違うクラスのembeddingの集合

.. math::
  :nowrap:

  \begin{align}
    L_{lifted} (\mathcal{X}) &:= \sum_{x_i \in \mathcal{X}}
      \left( \log \sum_{x_k \in \mathcal{X}_{x_i}^+} \exp(m - s(x_i, x_k)) + \log \sum_{x_k \in \mathcal{X}_{x_i}^-} \exp( s(x_i, x_k)) \right)
  \end{align}

- **Multi Similarity loss** [Wang19]_ :doc:`metriclearning/multi_similarity`

  - :math:`\alpha, \beta` : スケーリングパラメータ(ハイパーパラメータ)

.. math::
  :nowrap:

  \begin{align}
    L_{MS} (\mathcal{X}) &:= \cfrac{1}{|\mathcal{X}|} \left\{
    \cfrac{1}{\alpha} \log \left(1+ \sum_{x_k \in \mathcal{X}_{x_i}^+} \exp(-\alpha (s(x_i, x_k) - m)) \right)
    + \cfrac{1}{\beta} \log \left(1+ \sum_{x_k \in \mathcal{X}_{x_i}^-} \exp(\beta (s(x_i, x_k) - m)) \right) \right\}
  \end{align}

**Proxy族: 各クラスを代表するProxiesを使ったロス**

- **Proxy NCA** [Movshovitz17]_ :doc:`metriclearning/proxy_nca`

  - :math:`\mathcal{P} = \{p_1, \ldots, p_L \}`, proxies (trainableな変数として、backpropの対象にして学習していく, L=クラス数)
  - :math:`d` : 距離関数 (例: L2距離)

.. math::
  :nowrap:

  \begin{align}
    L_{NCA}(x) := -
    \log \cfrac{\exp(-d(x, p_y ))}
    {\sum_{p \in \mathcal{P} \setminus \{p_y\} } \exp( -d(x, p))}
  \end{align}

- **SoftTriplet** [Qian19]_

  - ProxyNCA like
  - proxyを各クラスK個用意して、relaxed similarityを導入している
  - softmax lossがsmoothedなtriplet lossであるとか言っていて興味深いが、詳しく読めていない

- **Proxy Anchor** [Kim20]_ :doc:`metriclearning/proxy_anchor`

  - :math:`\mathcal{P}^+, \mathcal{P}^-` : ミニバッチ内のデータのクラスのproxyの集合, ミニバッチ内のデータには存在しないクラスのproxyの集合
  - :math:`\mathcal{X}^+_p, \mathcal{X}^-_p` : ミニバッチ内のproxy pと同じクラスのembeddingの集合, ミニバッチ内のproxy pとは違うクラスのembeddingの集合
  - :math:`\alpha` : スケーリングパラメータ (ハイパーパラメータ)

.. math::
  :nowrap:

  \begin{align}
    L_{PA}(\mathcal{X}) := \cfrac{1}{|\mathcal{P}^+|}
    \sum_{p \in \mathcal{P}^+}
    \log \left(1 + \sum_{x \in \mathcal{X}^+_p} \exp(-\alpha (s(p, x) - m )) \right)
    + \frac{1}{|\mathcal{P}^-|}
    \sum_{p \in \mathcal{P}^-}
    \log \left(1 + \sum_{x \in \mathcal{X}^-_p} \exp(\alpha (s(p, x) + m )) \right)
  \end{align}


Classification losses
^^^^^^^^^^^^^^^^^^^^^^^^

- Center loss [Wen16]_

- SphereFace [Liu17]_

- CosFace [Wang18]_

- ArcFace [Deng19]_


参考文献
---------

.. [Hadsel06] R. Hadsell, S. Chopra, and Y. LeCun. Dimensionality reduction by learning an invariant mapping. In CVPR, 2006.

.. [Hoffer15] E. Hoffer and N. Ailon. Deep metric learning using triplet network. In SIMBAD, 2015.

.. [Sohn16] K. Sohn. Improved deep metric learning with multi-class n-pair loss objective. In NIPS 2016.

.. [Song16] H. Oh Song, Y. Xiang, S. Jegelka, and S. Savarese. Deep metric learning via lifted structured feature embedding. In CVPR, 2016.

.. [Wang19] X. Wang, X. Han, W. Huang, D. Dong, and M.R. Scott. Multi-similarity loss with general pair weighting for deep metric learning. In CVPR 2019.

.. [Movshovitz17] Y. Movshovitz-Attias, A. Toshev, T. K. Leung, S. Ioffe, and S. Singh. No fuss distance metric learning using proxies. In ICCV 2017.

.. [Qian19] Qi Qian, Lei Shang, Baigui Sun, Juhua Hu, Hao Li, Rong Jin. SoftTriple Loss: Deep Metric Learning Without Triplet Sampling. In ICCV, 2019.

.. [Kim20] S. Kim, D. Kim, M. Cho, and S. Kwak. Proxy Anchor Loss for Deep Metric Learning. In CVPR 2020.

.. [Wen16] Yandong Wen, Kaipeng Zhang, Zhifeng Li, Yu Qiao. A Discriminative Feature Learning Approach for Deep Face Recognition. In ECCV 2016.

.. [Liu17] Weiyang Liu, Yandong Wen, Zhiding Yu, Ming Li, Bhiksha Raj, Le Song. SphereFace: Deep Hypersphere Embedding for Face Recognition. In CVPR 2017.

.. [Wang18] Hao Wang, Yitong Wang, Zheng Zhou, Xing Ji, Dihong Gong, Jingchao Zhou, Zhifeng Li, Wei Liu. CosFace: Large Margin Cosine Loss for Deep Face Recognition. In CVPR 2018.

.. [Deng19] Jiankang Deng, Jia Guo, Niannan Xue, Stefanos Zafeiriou. ArcFace: Additive Angular Margin Loss for Deep Face Recognition. In CVPR 2019.

.. [Musgrave20] Kevin Musgrave, Serge Belongie, Ser-Nam Lim. A Metric Learning Reality Check. In ECCV 2020.
