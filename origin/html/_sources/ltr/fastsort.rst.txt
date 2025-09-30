Blondel ICML'20 Fast Differentiable Sorting and Ranking
====================================================================================================

https://arxiv.org/abs/2002.08871


著者 

- Mathieu Blondel (Google Research, Brain team)
- Olivier Teboul (Google Research, Brain team)
- Quentin Berthet (Google Research, Brain team)
- Josip Djolonga (Google Research, Brain team)

概要
-------

- sortやrankは線形計画問題
- それに正則化項(squared normとか)を加えると、置換多面上へのprojectionになる
- 置換多面上へのprojectionはisotonic regressionの問題として表現でき O(n log n) で計算できて、微分もできる

Sorting and ranking as linear programs
------------------------------------------------------------------

sortやrankは線形計画問題として表現する

|

直接的に表現してみると、 :math:`\rho := (n, n-1, \ldots, 1), \Sigma` を[n]のpermutationのすべてのパターンの集合 として

|

**LPにすると**

:math:`\mathcal{P}(w) := \text{conv}(\{ w_\sigma ~:~ \sigma \in \Sigma \})` (つまり :math:`w` を並び替えたもののと集合の凸包、 :math:`\mathcal{P}(\rho) = \text{conv}(\Sigma)` となる ) として

.. math::
  :nowrap:

  \begin{align}
    s(\theta) = \arg \max_{y \in P(\theta)} \langle y, \rho \rangle, ~~
    r(\theta) = \arg \max_{y \in P(\rho)} \langle y, - \theta \rangle,
  \end{align}


sortとrankを一般化しておく

.. math:: P(z,w) := \arg \max_{\mu \in \mathcal{P}(w)} \langle \mu, z \rangle

- sortは :math:`(z, w) = (\rho, \theta)`
- rankは :math:`(z, w) = (-\theta, \rho)`

Differentiable sorting and ranking
------------------------------------------------------------------

正則化項 :math:`Q(\mu) := \frac{1}{2} {\left\lVert \mu \right\rVert}^2` を加えると (論文中ではKL距離も紹介されているが、ここではsquared normだけ見る)


.. math:: P_{\epsilon Q} (z/\epsilon, w) :=  \arg \max_{\mu \in \mathcal{P}(w)} \langle \mu, z/\epsilon \rangle - Q(\mu) = \arg \min_{\mu \in \mathcal{P}(w)} \frac{1}{2} {\left\lVert \mu - z/\epsilon \right\rVert}^2

となり、 :math:`z` の :math:`\mathcal{P}(w)` 上へのprojectionになる。


正則化パラメータ :math:`\epsilon` を調整すると (なんか論文中の :math:`\epsilon` と定義が違う気がするが)


.. image:: ../img/ltr/ltr_fastsort_fig2.png
  :scale: 80%
  :align: center

**Properties**

- Differentiability: :math:`s_Q(\theta), r_Q(\theta)` は :math:`\theta` について微分可能
- Order preservation: :math:`0 < \theta < \infty` で :math:`s:=s_Q(\theta), r:=r_Q(\theta), \sigma := \sigma(\theta)` としたとき :math:`s_1 \ge s_2 \ge \cdots s_n, r_{\sigma_1} \le r_{\sigma_2} \le \cdots \le r_{\sigma_n}` となる




Fast computation and differentiation
---------------------------------------------------------------

ここでは、単純なチェーン制約を利用できて projectionがisotonic optimizationとして表現できる。

(:math:`\sigma(z), \sigma^{-1}(z)` が登場するが、sortのときは :math:`z = \rho` だが、 rankのときは :math:`z=-\theta` になってしまうのでまずいのでは・・・？)

.. math::
  :nowrap:

  \begin{align}
    & P_Q (z, w) := z - v_Q (z_{\sigma(z)}, w)_{ \sigma^{-1}(z) } \\
    & ~ \text{where}~~
    v_Q (s, w) := \arg \min_{v_1 \ge \cdots \ge v_n} \frac{1}{2} {\left\lVert v - (s-w) \right\rVert}^2
  \end{align}

|

:math:`v_Q` は古典的に知られているように isotonoic regressionで、PAV algorithmでexactに解ける。(計算コストは :math:`O(n)` )


|

(時間なくて導出追えていないので、よくわかりません。あとで見ておきます)



著者による実装
------------------

https://github.com/google-research/fast-soft-sort/


.. include:: fastsort_demo.ipynb
   :parser: myst_nb.docutils_

