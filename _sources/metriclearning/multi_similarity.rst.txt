Wang CVPR19 Multi-Similarity Loss with General Pair Weighting for Deep Metric Learning
=========================================================================================

https://arxiv.org/abs/1904.06627

著者 (全員 Malong Technologies )

- Xun Wang
- Xintong Han
- Weiling Huang
- Dengke Dong
- Matthew R. Scott

概要
-------

- :math:`\alpha, \beta` : スケーリングパラメータ(ハイパーパラメータ)

.. math::
  :nowrap:

  \begin{align}
    L_{MS} (\mathcal{X}) &:= \cfrac{1}{|\mathcal{X}|} \left\{
    \cfrac{1}{\alpha} \log \left(1+ \sum_{x_k \in \mathcal{X}_{x_i}^+} \exp(-\alpha (s(x_i, x_k) - m)) \right)
    + \cfrac{1}{\beta} \log \left(1+ \sum_{x_k \in \mathcal{X}_{x_i}^-} \exp(\beta (s(x_i, x_k) - m)) \right) \right\}
  \end{align}

**著者らの主張**

- relative similaritiesの性質は3つある ( :math:`w_{ij} := \partial L / \partial s(x_i, x_j)` とする )

  - Simirarity-S

    - :math:`y_i \neq y_j` で Sij (iとjの類似度)が大きくなった時, :math:`w_{ij}` は大きなるべき

  - Simirarity-P

    - :math:`y_k = y_i  \neq y_j` で Sij < Sik のときより Sij > Sik のときのほうが :math:`w_{ij}` 相対的に大きなるべき

  - Simirarity-N

    - :math:`y_k \neq y_i  \neq y_j` で Sij < Sik のときより Sij > Sik のときのほうが :math:`w_{ij}` は相対的に大きなるべき

.. image:: ../img/ml/ms_f2.png
  :scale: 40%
  :align: center

Metric learningのロスたちはそれらの性質を持っているのか?

.. image:: ../img/ml/ms_t1.png
  :scale: 40%
  :align: center


Multi Similarty lossについて

.. math::
  :nowrap:

  \begin{align}
    w^{-}_{ij} = \frac{1}{\exp(\beta(m - s(x_i, x_j))
      + \sum_{x_k \in \mathcal{X}_{x_i}^- } \exp(\beta(s(x_i, x_k) - s(x_i, x_j))) }
      = \frac{\exp(\beta(m - s(x_i, x_j))}{1 + \sum_{x_k \in \mathcal{X}_{x_i}^- } \exp(\beta(s(x_i, x_j) - s(x_i, x_k))) }
  \end{align}

- :math:`w^{-}_{ij}` はnegativeのほうの項をSijで微分したっぽい、論文中には定義はない
- これで、Similarity-S, Simirality-Nは満たしていると言っている
- Similarity-Pの方はどうなのか :math:`w^{+}_{ij}` をみてもだめっぽい

.. math::
  :nowrap:

  \begin{align}
    w^{-}_{ij} = \frac{1}{\exp(-\alpha(m - s(x_i, x_j))
      + \sum_{x_k \in \mathcal{X}_{x_i}^- } \exp(-\alpha(s(x_i, x_k) - s(x_i, x_j))) }
  \end{align}

- Pair-miningをSimiratity-Pに基づいて行うからOKだと言っている

  - negative pairは、 :math:`S^{-}_{ij} > \min_{y_i = y_k} S_{ik} - \epsilon` を満たすペアを学習に使う
  - positivef pairは :math:`S^{+}_{ij} < \max_{y_i \neq y_k} S_{ik} + \epsilon` を満たすペアを学習に使う

実験
------

- 比較手法の精度をどうやって持ってきているのか書いてない、実験設定そろってない論文?

**CUB-200 & Cars196**

.. image:: ../img/ml/ms_t3.png
  :scale: 40%
  :align: center

**SOP**

.. image:: ../img/ml/ms_t5.png
  :scale: 40%
  :align: center


Wang CVPR'20 Cross-Batch Memory for Embedding Learning
============================================================

https://arxiv.org/abs/1912.06798

著者 (全員 Malong Technologies )


- Xun Wang
- Haozhi Zhang
- Weilin Huang
- Matthew R. Scott

概要
------

**アイデア**

- 過去のminibatchで計算しておいた、embeddingを保持しておいてそれとのロスを計算させよう

.. image:: ../img/ml/xbm_a1.png
  :scale: 40%
  :align: center

実験
-------

- contrastiveが一番いい・・・
- MSの伸びが悪いのは外れ値の可能性がある極端な hard-negative の重みが高いためとい言っている


.. image:: ../img/ml/xbm_t1.png
  :scale: 40%
  :align: center



