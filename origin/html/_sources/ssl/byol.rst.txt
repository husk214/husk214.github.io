Grill NIPS'20 BYOL (Bootstrap Your Own Latent A New Approach to Self-Supervised Learning)
========================================================================================================================

- 著者: Jean-Bastien Grill*,(1) Florian Strub*,(1) Florent Altché*,(1) Corentin Tallec*,(1) Pierre H. Richemond*,(1,2) Elena Buchatskaya(1) Carl Doersch(1) Bernardo Avila Pires(1) Zhaohan Daniel Guo(1) Mohammad Gheshlaghi Azar(1) Bilal Piot(1) Koray Kavukcuoglu(1) Rémi Munos(1) Michal Valko(1)

  1. DeepMind
  2. Imperial College

-  https://arxiv.org/pdf/2006.07733.pdf


Abstract
------------

- **Negative pairなしで** SimCLR超え

.. image:: ../img/ssl/boyl_fig1.png
  :scale: 80%
  :align: center

SimCLRより、batch size減らしても精度劣化しないし、AugmentationをSimpleにしていっても精度劣化しない

.. image:: ../img/ssl/boyl_fig3.png
  :scale: 80%
  :align: center


Algorithm
-------------

準備

- online側とtarget側という２つの初期値が一緒のencoder :math:`f_\theta, f_\xi` , projection :math:`g_\theta, g_\xi` を用意

  - encoderはResNetとか、projectionはMLP

- online側にだけ prediction :math:`q_\theta` (例えばMLP) を用意


以下繰り返し

- 同じ画像を別々のAugmentationして (:math:`v, v'`)、それぞれをonline側とtarget側に流して出力を得る
- target側のネットワークはstop gradientする
- online側とtarget側の出力の距離を最小化する　(online側だけ更新)

  - 厳密にはonlineとtargetの入力を入れ替えて同じことをして、入れ替えていないものと和をとったものを損失関数とする

- target側をmomentum updateする : :math:`\xi \leftarrow \tau \xi + (1-\tau) \theta`


.. image:: ../img/ssl/boyl_fig2.png
  :scale: 60%
  :align: center


positive pairの距離だけを最小化するのであれば、ネットワークは常に定数を出力するようになってしまえばよいので簡単に学習は崩壊してしまいそう。

なぜBYOLは崩壊しないのか? → よくわかんない

読んでないけどその疑問にタックルした論文: http://proceedings.mlr.press/v139/tian21a/tian21a.pdf (ICML'21)
