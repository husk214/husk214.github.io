Roth ICML'21 Simultaneous Similarity-based Self-Distillation for Deep Metric Learning
=============================================================================================

- 著者 : Karsten Roth (1), Timo Milbich (2), Bjorn Ommer (2), Joseph Paul Cohen (3), Marzyeh Ghassemi (4,1)

  - 1: University of Toronto, 2: Heidelberg University, 3:  Universite de Montreal, 4: MIT

- https://proceedings.mlr.press/v139/roth21a/roth21a.pdf

Abstract 
-------------

(NotebookLMさんに要約してもらいました)

- 深層距離学習（DML）は、画像検索や顔認識などの分野で重要な役割を果たしていますが、従来の手法では、埋め込み空間の次元数が大きくなると、検索コストが増加するという問題がありました。
- 本論文で提案されたSimultaneous Similarity-based Self-Distillation (S2SD)は、高次元埋め込み空間の情報を活用しながら、低次元埋め込み空間の学習を可能にすることで、この問題を解決する新しい学習手法です。
- S2SDは、低次元埋め込み空間の学習と並行して、複数の高次元埋め込み空間を学習します。
- そして、高次元空間におけるサンプル間の関係性（類似度）を、知識蒸留によって低次元空間に転移します。 これにより、高次元空間の豊かな表現力を活用しながら、検索効率の高い低次元埋め込み空間を学習できます。
- S2SDの重要な点は、知識蒸留を、従来のように別の教師モデルを用いるのではなく、同じネットワーク構造内で、単一の学習プロセスで行う点です。
- 具体的には、高次元空間におけるサンプル間の類似度を表す行列と、低次元空間における類似度行列とのKLダイバージェンスを最小化するように学習を行います。
- さらに、S2SDは、複数の異なる次元を持つ高次元空間を用いることで、蒸留される情報の再利用性を促進し、汎化性能を向上させています。 これは、複数のタスクで再利用可能な特徴が、より汎化しやすいという知見に基づいています。


提案法
---------


.. image:: ../img/ml/s2sd_fig1.png
  :scale: 60%
  :align: center


- この図の通りでbackboneは共通でその先に異なる次元数のMLPを用意しておいて類似度行列のKLロスを加える
- 実験でやっている次元数は [512, 1024, 1536, 2048]

実験結果
----------

.. image:: ../img/ml/s2sd_tab1.png
  :scale: 100%
  :align: center
