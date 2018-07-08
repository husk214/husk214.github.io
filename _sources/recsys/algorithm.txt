Algorithm
============

[Liu]_ によるとランク学習のアルゴリズムPointwise, Pairwise, Listwise Approchの3つに分類される.


Pointwise Approch
-------------------

- クエリ :math:`q_i` のインデックス :math:`i`  を無視して、 だた予測した関連度と教師の関連度の差の最小化を目指す

- 例えば以下のような感じで, 二乗誤差最小化問題として定式化し、 モデル :math:`f`  を学習する

.. raw:: html

  \begin{align}
    \min_{f} \sum_{i=1}^{n} \sum_{j=1}^{n_i}
    (f(x_i^{(j)}) - y_i^{(j)})^2
  \end{align}


- つまり、ただの回帰問題としてランク学習をするアプローチ


Pairwise Approch
-------------------

- 関連文書のペア :math:`\{ x_i^{(j)}, x_i^{(k)} \}` を与えてどちらの文書の関連度が高いかの2値分類問題としてランク学習するアプローチ


Listwise Approch
-------------------

- リストに対して損失関数を定義し、それの最小化を目指すアプローチ


.. [Liu] Liu, Tie-Yan. "Learning to rank for information retrieval." Foundations and Trends® in Information Retrieval 3.3 (2009): 225-331.

