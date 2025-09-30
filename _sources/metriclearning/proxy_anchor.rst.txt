Kim CVPR'20 Proxy Anchor Loss for Deep Metric Learning
========================================================

https://arxiv.org/abs/2003.13911

著者 (全員 POSTECH, Pohang, Korea)

- Sungyeon Kim
- Dongwon Kim Minsu Cho
- Suha Kwak

概要
------

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

**著者らの主張**

.. image:: ../img/ml/pa_f2.png
  :scale: 40%
  :align: center


(a) Triplet : 組み合わせの総数多すぎ、学習に効くペアを見つけられていない
(b) N-pair : Tripletより一度に全体を見れるが、データ全体とは言えない
(c) Lifted Structure: N-pairよりよいが、まだ全体ではない
(d) Proxy-NCA: 収束ははやいが、データ全体の情報は使えていない (a-cようなリッチなペア組み合わせ)
(e) Proxy Anchor: Proxyも使うし、 a-cのようなサンプル間のペアも学習に使う

**Cars196での実験**

- 収束がはやいし、精度も高い

.. image:: ../img/ml/pa_f1.png
  :scale: 40%
  :align: center


実験
------

- 実験設定そろってない論文?

**CUB-200 & Cars196**

.. image:: ../img/ml/pa_t2.png
  :scale: 40%
  :align: center

**SOP**

.. image:: ../img/ml/pa_t3.png
  :scale: 40%
  :align: center

