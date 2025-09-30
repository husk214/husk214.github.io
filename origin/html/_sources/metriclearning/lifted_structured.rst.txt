Song CVPR'16 Deep Metric Learning via Lifted Structured Feature Embedding
=========================================================================================

https://arxiv.org/abs/1511.06452

著者

- Hyun Oh Song (Stanford)
- Yu Xiang (Stanford)
- Stefanie Jegelka (MIT)
- Silvio Savarese (Stanford)

概要
-------

- :math:`\mathcal{X}` : ミニバッチ (embeddingの集合)
- :math:`\mathcal{X}^+_{x_i}` : ミニバッチ内の :math:`x_i` と同じクラスのembeddingの集合
- :math:`\mathcal{X}^-_p` : ミニバッチ内の :math:`x_i` とは違うクラスのembeddingの集合

.. math::
  :nowrap:

  \begin{align}
    L_{lifted} (\mathcal{X}) &:= \sum_{x_i \in \mathcal{X}}
      \left( \log \sum_{x_k \in \mathcal{X}_{x_i}^+} \exp(m - s(x_i, x_k)) + \log \sum_{x_k \in \mathcal{X}_{x_i}^-} \exp( s(x_i, x_k)) \right)
  \end{align}


**著者らの主張**

.. image:: ../img/ml/lifted_structure_f5.png
  :scale: 40%
  :align: center

- 線の意味

  - 青の線: negative pairとの距離
  - 赤の線: positive pairとの距離
  - 灰色の曲線: マージン境界 (外側ではロス=0)
  - 矢印の方向: 勾配の方向

- (a) Constructive loss

  - 損失関数によりnegative pairとの距離を広げようとするため，anchorは同じクラスから押し出される

- (b) Triplet loss

  - 同様にanchorは同じクラスから押し出される (なんでこうなるのかまったく理解できない)

- (c) Lifted Structure loss

  - negative pair をミニバッチに複数含めているため，正しい方向に勾配を進めることができる

**感想**

- constructive lossもミニバッチを考慮すれば、以下のようになるので、著者らの主張が理解できない

.. math::
  :nowrap:

  \begin{align}
    L_{constructive} (\mathcal{X}) &:= \sum_  {x_i \in \mathcal{X}}
      \left( \sum_{x_k \in \mathcal{X}_{x_i}^+} [m_p - s(x_i, x_k)]_+ + \sum_{x_k \in \mathcal{X}_{x_i}^-}  [s(x_i, x_k) - m_n]_+ \right)
  \end{align}

