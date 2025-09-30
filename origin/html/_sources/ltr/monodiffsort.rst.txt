Petersen ICLR'22 Monotonic Differentiable Sorting Networks
====================================================================================================

https://openreview.net/forum?id=IcUWShptD7d

著者 

- Felix Petersen (University of Konstanz)
- Christian Borgelt (University of Salzburg)
- Hilde Kuehne (University of Frankfurt, MIT-IBM Watson AI)
- Oliver Deussen (University of Konstanz)

概要
-------

- Differentiable Sorting Networks (ICML'21) の著者らによる改良版
- 学習において関数の単調性が重要 (ちょっと疑問、論文中でも軽く議論されているだけ)
- Differentiable Sorting Networksで導入したmin, maxをrelaxedしたものが単調になるように関数を設計すると精度がよくなる

Theory
----------------------

|

- 「min, maxをrelaxedしたものが単調になる」の定義をする
- それを達成する関数の条件を見る
- また緩和したmin, maxと真のmin, maxの誤差をバウンドするための条件も見る

|

**Definition 1 (Sigmoid Function)**

sigmoid(つまりS字の)関数を連続単調非減少で入力=0.5あたりで対称になる関数 :math:`f` として定義する。

.. math:: f: \mathbb{R} \rightarrow [0, 1] ~~ \text{with} ~~ \lim_{x\rightarrow -\infty} f(x) = 0 ~~ \text{and} ~~ \lim_{x\rightarrow \infty} f(x) = 1

|

**Definition 2 (Continuous Conditional Swaps)**

sigmoid関数 :math:`f` についてのcontinuous conditional swapを次のように定義する

.. math::
  :nowrap:

  \begin{align}
    \text{min}_f (a, b) &= a f(b-a) + b (a-b), ~~ \text{max}_f (a, b) =  a f(a-b) + b (b-a) 
  \end{align}

|

**Definition 4 (Monotonic Continuous Conditional Swaps)**

:math:`\text{min}_f (x, 0) \ge 0, ~~ \forall x` が成り立つとき、 :math:`f` がmonotonic conditional swapを生成するという。

|

**Theorem 5 (Monotonicity of Continuous Conditional Swaps)**

:math:`f` が 非減少monotonic conditional swapを生成するには、導関数が :math:`1/x^2` より早く減退しない必要。つまり、

.. math :: f'(x) \in \Omega \left(\frac{1}{x^2} \right).


|


**Definition 7 (Error-Bounded Continuous Conditional Swaps).**

Continuous conditional swapsは :math:`\sup_x \min_{f} (x, 0) = c` が有限である場合に限り、bounded errorを持つ。またその Continuous conditional swapsを :math:`c` の error boundedを持つという。

**Theorem 8 (Error-Bounds of Continuous Conditional Swaps)**

もし式 :eq:`mds_eq8` が成り立つならばContinuous conditional swapsはbounded errorを持つ。

.. math:: f'(x) \in \mathcal{O} \left(\frac{1}{x^2} \right)
   :label: mds_eq8


さらに単調である場合、誤差の境界は :math:`\lim_{x \rightarrow \infty} \min_f (x, 0)` として求められ、さらに式 :eq:`mds_eq8` が成り立つ場合にのみエラーがboundされる。

Sigmoid Functions
---------------------


:ref:`labelDiffSortNet` で提案された logistic sigmoid :math:`\sigma(x) := 1 / (1 + \exp(-\beta x))` は error boundはあるが、monotonic conditional swapにはならない。 (Fig.2の青線)

|


.. image:: ../img/ltr/ltr_monodsn_fig2.png
  :scale: 40%
  :align: center

|

ここではerror boundがあってmonotonic conditional swapとなる :math:`f` を3つ見ていく。

|

**Reciprocal Sigmoid Function**

:math:`f` が error boundを持つ非減少monotonic conditional swapを生成するには、Theorem 5と8より :math:`f'(x) \in \Theta \left(1/x^2 \right)` となる必要があるので、:math:`f_{\mathcal{R}}' (x) = \cfrac{1}{(2|x| + 1)^2}` は自然な選択で、:math:`f_{\mathcal{R}}` は以下で、 誤差は :math:`\epsilon =0.25` となる。

.. math::  f_{\mathcal{R}}(x) = \int_{-\infty}^{x} \cfrac{1}{(2\beta |t| + 1)^2} dt = \cfrac{1}{2} \cfrac{2\beta x}{1 + 2\beta |x| } + \cfrac{1}{2}

:math:`\min(x, 0) ~ \forall x > 0` は0であることが望ましいので、:math:`\min_f(x, 0)` を減らすことを考えていく。

|

**Cauchy distributions**

Cauchy distributionの累積分布関数を使うことで誤差を :math:`\epsilon = 1/\pi^2` へ減らすことができる。

.. math::  f_{\mathcal{C}}(x) = \int_{-\infty}^{x} \cfrac{\beta}{1 + (\beta)^2} dt = \cfrac{1}{\pi} \arctan (\beta x) + \cfrac{1}{2}

|

**Optimal Monotonic Sigmoid Function**

誤差限界を達成し、monotonicかつ1-Lipschitz continuousなconditional swapとなる :math:`f_{\mathcal{O}}` は以下になる。

.. math::
  :nowrap:

  \begin{align}
  f_{\mathcal{O}}(x) =
    \left\{
    \begin{array}{ll}
      -\frac{1}{16 \beta x} & \text{if} ~~ \beta x < -\frac{1}{4} \\
      1 -\frac{1}{16 \beta x} & \text{if} ~~ \beta x > \frac{1}{4} \\
      \beta x + \frac{1}{2} & \text{otherwise}.
    \end{array}
    \right.
  \end{align}

論文中に証明あり (Theorem 10)

|

Fig.3は 3-wire odd-even sorting newtorkで logistic sigmoid(左)とoptimal sigmoid(右)のロスをプロットしたもの。

logistic sigmoidの場合、(3 , 2, 1)でランクの1つが正しいにもかかわらず、 すべてのランクが異なる(2, 3, 1)と同じ損失になってしまっている。

.. image:: ../img/ltr/ltr_monodsn_fig3.png
  :scale: 60%
  :align: center



Monotonicity of Other Differentiable Sorting Operators
---------------------------------------------------------------

- 既存手法の :math:`\min(x, 0)` がどうなっているか見てみる。
- 他の手法の :math:`\min(x, 0)` ってなにかというと、 softsortをdifferentiableなsort, 入力を :math:`s=[0, x]` として :math:`\min(\text{softsort(s)})` の値を見る

.. image:: ../img/ltr/ltr_monodsn_fig4.png
  :scale: 40%
  :align: center

- FastSortはmonotonicだが一定の値を超えると線形にエラーが伸びていく

|

実際にプロットしてみる。

.. include:: not_monotonic_demo.ipynb
   :parser: myst_nb.docutils_


Empirical Evaluation
-------------------------

Differentiableなsort論文で毎回やられている実験で性能比較

- MNISTやSVHNを4桁の数字になるように並べ、:math:`n` 個を1セットにして、ソートするモデルをend-to-endで学習する
- そのソートの正答率で各手法を比較する

イメージは↓の画像のtask 1 (Grover ICLR'19のFig. 4)

.. image:: ../img/ltr/ltr_ns_fig4.png
  :scale: 60%
  :align: center

|

結果 (数値は5回実行した結果の平均で、カッコ)

- 数値はすべての要素が正確にソートされている割合、カッコ内の数値は個別に見たときにランクがあっている割合 (5回実行した結果の平均)
- Diffsort (Logistic with Activation Replacement Trick) も結構強いが、この論文で提案されているもののほうが強い

.. image:: ../img/ltr/ltr_monodsn_tab3.png
  :scale: 80%
  :align: center


