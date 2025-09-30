==================================
Self Supervised Learning (SSL)
==================================

- SSLの目的: 教師なしでいい感じの表現学習したい
- SSLの手法の評価方法:

  - Linear Evaluation: SSLしたモデルの出力を特徴量に線形モデルを学習して精度を測る
  - Fine Tuning Task: SSLを事前学習として、教師データを使って fine tuneして精度を測る

SSLだけで完結するわけではない

***********************
Papers
***********************


.. toctree::
  :maxdepth: 1

  ssl/simclr.rst
  ssl/byol.rst
  ssl/simsiam.rst
  ssl/how_avoid.rst
