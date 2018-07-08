Metric
===========

Notation
----------
.. raw:: html

- :math:`r \in \mathbb{R}^n` : (アルゴリズムの予測値によってソートした)関連度のリスト


nDCG@k
----------
- いくつかの定義が存在している
- 関連度のリストに対して計算される
- nDCGは、normalized Discounted Cumulative Gainの略でDCGを正規化したもの
- nDCG := DCG / IdealDCG

  + DCG := アルゴリズムの予測値によってソートした関連度リストを下位になればなるほど割引して足し上げた値
  +  IdealDCG := 関連度自身でソートしたリストのDCG

.. raw:: html

  \begin{align}
    \label{eq:ndcg1}
    \text{DCG@}k &:= \sum_{i=1}^{k} \frac{r_i}{\log_2 (i+1)} \\
    \label{eq:ndcg2}
    \text{DCG@}k &:= \sum_{i=1}^{k} \frac{2^{r_i} - 1}{\log_2 (i+1)}
  \end{align}


- 本来のnDCGは [Kalervo]_ によって(1)と似た, (3)のように導入されたが、logの底が2の場合rank = 1と同様に rank=2も割引されないため、明示的にそのように意図しないのであれば(1)の定義を用いることが自然に思える

.. raw:: html

  \begin{align}
    \text{DCG@}k := r_1 + \sum_{i=2}^{k} \frac{r_i}{\log_2 i}
  \end{align}

- 式(2) は [Burges]_ によって導入され, 見ての通り 2の関連度乗を足しているので (1)よりも, より関連度の高いものを当てることに重きをおいており、xgboost, LightGBMも採用している


CatBoostのDCGの計算方法
^^^^^^^^^^^^^^^^^^^^^^^^^^
- CatBoostは式(1)のDCGの定義を採用しているが、DCG := 0.5 (OptimisticDCG + PessimisticDCG) と計算している

  + OptimisticDCG := アルゴリズムの予測値でソートするとき、同じ予測値なら関連度が高い方を上位とした関連度リストを入力としたDCG
  + PessimisticDCG := アルゴリズムの予測値でソートするとき、同じ予測値なら関連度が低い方を上位とした関連度リストを入力としたDCG

- このように計算したほうが、よさげに見える



.. [Kalervo] Järvelin, Kalervo, and Jaana Kekäläinen. "Cumulated gain-based evaluation of IR techniques." ACM Transactions on Information Systems (TOIS) 20.4 (2002): 422-446.

.. [Burges] Burges, Chris, et al. "Learning to rank using gradient descent." Proceedings of the 22nd international conference on Machine learning. ACM, 2005.
