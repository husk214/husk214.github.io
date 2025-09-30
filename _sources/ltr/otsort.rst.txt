Cuturi NeurIPS'19 Differentiable Ranks and Sorting using Optimal Transport
=========================================================================================

https://arxiv.org/abs/1905.11885

著者 

- Marco Cuturi (Google Research, Brain Team)
- Olivier Teboul (Google Research, Brain Team)
- Jean-Philippe Vert (Google Research, Brain Team)

概要
-------

- sortは最適輸送問題の一種
- (正則化をした)最適輸送の問題はsinkhorn algorithmで解ける
- sinkhorn algorithmは行列演算で微分可能な手続きなので、sortも微分可能になりend-to-endで学習できる

前置き
----------------------

最適輸送については以下あたりを読むと良さそう

- 最適輸送の理論とアルゴリズム (佐藤竜馬) (機械学習プロフェッショナルシリーズ)　https://www.kspub.co.jp/book/detail/5305140.html
- Optimal transport for applied mathematicians (Filippo Santambrogio)
- Computational Optimal Transport (Gabriel Peyré and Marco Cuturi) https://arxiv.org/abs/1803.00567

|

**最適輸送の定式化** 

.. math:: \min_{P \in U(a, b) } \langle C, P \rangle, ~~~ \text{where} ~~ U(a, b) := \{P \in \mathbb{R}^{n\times m}_{+} \mid P \mathbb{1}_m  = a, ~ P^{\top}\mathbb{1}_n = b \}
   :label: otsort_eq1
|

最適化問題のイメージ 

- 倉庫がn個、工場がm個あり、倉庫iには材料が :math:`a_i` あって、工場jは材料を :math:`b_j` 必要としている。
- 輸送コスト倉庫iから倉庫jへの輸送コストを :math:`C_{ij}` とする。
- そのとき、輸送コストが最小になる輸送を求めたい。

|

**エントロピー正則化とシンクホーンアルゴリズム**

最適輸送の理論とアルゴリズム (佐藤竜馬) の3章より

- 最適輸送を線形計画問題として定式化したがいくつか問題点がある

  - 線形計画ソルバー計算量の問題(最悪入力サイズの3乗)
  - 組み合わせてend-to-endでの学習はできない
  - :math:`a, b, C` について滑らかでないので微分できない

- そこでエントロピー正則化をつけた最適輸送問題を導入すると、その問題はiterativeな行列演算で解ける
- ということは自動微分できて、end-to-endな学習に組み込める

エントロピー正則化つき最適輸送問題

.. math:: \min_{P \in U(a, b) } \left[ \langle C, P \rangle + \epsilon \sum_i^n \sum_j^m P_{ij} ((\log P_{ij} - 1)) \right]
   :label: ot_ent
|

シンクホーンアルゴリズム

1. :math:`A = \exp(-C/\epsilon), ~ u^{(0)} \leftarrow \mathbb{1}_n,~ v^{(0)} \leftarrow \frac{1}{{\lVert A \rVert}_1 } \mathbb{1}_m`
2. for :math:`k=1,2,\ldots` do
3. :math:`~~~~~ u^{(k)} \leftarrow \frac{a}{Ay^{(k-1)}}, ~ v^{(k)} \leftarrow \frac{b}{A^\top u^{(k)}}`

|


- シンクホーンアルゴリズムは :eq:`ot_ent` の最適解に収束する (最適輸送の理論とアルゴリズム (佐藤竜馬) の定理3.9)
- :math:`\epsilon` を十分小さくすれば、エントロピー正則化しない問題の最適解に近い解を得られることを示せる (最適輸送の理論とアルゴリズム (佐藤竜馬) の定理3.16)
- end-to-endの学習に組み込むとき、イテレーション回数は :math:`1, 2, \ldots 10` あたりにすることが多いらしい


Ranking and Sorting as an Optimal Transport Problem
---------------------------------------------------------

**Proposition 2(ソートは最適輸送の一種)**

- :math:`\mathbb{O}_n \subset \mathbb{R}^n` を長さnのincreasing vectorの集合とする。 (例えば :math:`[1.2, 2.4, 4.3] \in \mathbb{O}_3` )
- また、:math:`x` を対象の長さnのベクトル、 :math:`y \in \mathbb{O}_n` , :math:`h` を非負な値を取る関数として、 :math:`C_{ij} = h(y_j - x_i)` とする。
- そして、:math:`n=m, a = b = \mathbb{1}_n / n` とし、 :math:`h` を狭義凸関数、 :math:`P_{\star}` を :eq:`otsort_eq1` の最適解としたとき、以下が成り立つ。 


.. math:: \text{rank}(x) = n^2 P_{\star} \bar{b}, ~~ \text{sort}(x) = nP_{\star}^{\top} x, ~~~ \text{where} ~ \bar{b} := [1, \ldots, n]^\top


補足: ここでのrank, sortは昇順。降順にするなら、:math:`y` をdecreasing vectorにすればよい。

|

:math:`\epsilon` を動かしたときに 緩和版rankと緩和版sortの出力がどうなるかを示したものがFig.2 

- 左の図がsort対象のベクトルの要素の値
- 中央の図がrankがどう変化していくか(色は左の図の要素の色に対応)
- 右の図が緩和版sort関数の出力がどうなるか (色が:math:`\epsilon`, 真のsortが◯)

.. image:: ../img/ltr/ltr_otsort_fig2.png
  :scale: 80%
  :align: center



|

tensorflowで実装すると以下のような感じ。

.. include:: otsort_demo.ipynb
   :parser: myst_nb.docutils_
