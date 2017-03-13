.. Atsushi Shibagaki documentation master file, created by
   sphinx-quickstart on Sat Jun 11 10:51:18 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. role:: underline
  :class: underline

.. role:: pubs
  :class: pubs

.. raw:: html

  <figure class="top_float">
    <img src="_static/logo.jpg" class="img-thumbnail">
  </figure>

Atsushi Shibagaki (柴垣篤志)
==========================================
..
  I am currently a master's student
  (department of scientific and engineering simulation)
  in `Takeuchi lab <http://www-als.ics.nitech.ac.jp>`_,
  `Nagoya Institute of Technology <http://www.nitech.ac.jp>`_, Japan.

I found employment.

.. raw:: html

  <div class="contact">
  <span class="octicon octicon-mail"></span> <font color='#7ca428'>shibagaki.a.mllab.nit <span class="octicon octicon-mention"></span>
  gmail.com </font> <br>
  <span class="octicon octicon-mark-github"></span> <a href="https://github.com/husk214">GitHub</a>
  </div>

Publications
^^^^^^^^^^^^^^

.. :pubs:`Preprint`

:pubs:`International Conferences (refereed)`

.. raw:: html

    <div class="menu">
        <label for="Panel1">
        <strong>Simultaneous Safe Screening of Features and Samples in Doubly Sparse Modeling</strong> <br>
        <u><i>A. Shibagaki</i>, M. Karasuyama, K. Hatano and I. Takeuchi</u> <br>
        Proceedings of The 33rd International Conference on Machine Learning (<a href="http://icml.cc/2016/">ICML2016</a>), pp. 1577–1586, New York, NYC, USA, June 2016 <i>(acceptance rate = 322/1327 = 24.3%)</i> <br>
        <div class="mybtn3"><a href="http://jmlr.org/proceedings/papers/v48/shibagaki16.html">paper</a></div>
        <div class="mybtn3"><a href="http://arxiv.org/abs/1602.02485">arXiv</a></div>
        <div class="mybtn3"><a href="https://github.com/husk214/s3fs">code</a></div> <br>
        </label>
        <input type="checkbox" id="Panel1" class="on-off"/>
        <ul> <div class="abst"> <b>Abstract: </b>
        The problem of learning a sparse model is conceptually interpreted as the process of identifying active features/samples and then optimizing the model over them. Recently introduced safe screening allows us to identify a part of nonactive features/samples. So far, safe screening has been individually studied either for feature screening or for sample screening. In this paper, we introduce a new approach for safely screening features and samples simultaneously by alternatively iterating feature and sample screening steps. A significant advantage of considering them simultaneously rather than individually is that they have a synergy effect in the sense that the results of the previous safe feature screening can be exploited for improving the next safe sample screening performances, and viceversa. We first theoretically investigate the synergy effect, and then illustrate the practical advantage through intensive numerical experiments for problems with large numbers of features and samples. </div> </ul> <br>
        <label for="Panel2">
        <strong>Regularization Path of Cross-Validation Error Lower Bounds</strong> <br>
        <u><i>A. Shibagaki</i>, Y. Suzuki, M. Karasuyama and I. Takeuchi</u> <br>
         Proceedings of the 29th Neural Information Processing Systems (<a href="https://nips.cc/Conferences/2015">NIPS2015</a>), pp. 1666-1674, Montreal, Quebec, Canada, December 2015 <i>(acceptance rate = 403/1838 = 21.9 % )</i> <br>
        <div class="mybtn3"><a href="http://papers.nips.cc/paper/5817-regularization-path-of-cross-validation-error-lower-bounds">paper</a></div>
        <div class="mybtn3"><a href="http://arxiv.org/abs/1602.02485">arXiv</a></div>
        <div class="mybtn3"><a href="misc/shibagaki_poster_nips15.pdf">poster</a></div> <br>
        </label>
        <input type="checkbox" id="Panel2" class="on-off"/>
        <ul> <div class="abst"> <b>Abstract: </b>
        Careful tuning of a regularization parameter is indispensable in many machine learning tasks because it has a significant impact on generalization performances. Nevertheless, current practice of regularization parameter tuning is more of an art than a science, e.g., it is hard to tell how many grid-points would be needed in cross-validation (CV) for obtaining a solution with sufficiently small CV error. In this paper we propose a novel framework for computing a lower bound of the CV errors as a function of the regularization parameter, which we call regularization path of CV error lower bounds. The proposed framework can be used for providing a theoretical approximation guarantee on a set of solutions in the sense that how far the CV error of the current best solution could be away from best possible CV error in the entire range of the regularization parameters. Our numerical experiments demonstrate that a theoretically guaranteed choice of a regularization parameter in the above sense is possible with reasonable computational costs. </div> </ul> <br>
    </div>

:pubs:`Domestic Conferences (not refereed)`

.. raw:: html

    <div class="papercard">
        <strong>変数の保持と削除に関するセーフルールによるスパースモデル最適化問題のサイズ縮小と高速化に関する一考察</strong> <br>
        <u>烏山昌幸, <i>柴垣篤志</i>, 竹内一郎</u> <br>
        信学技報, vol. 116, no. 500, <a href="http://ibisml.org/ibisml028">IBISML</a> 2016-107, pp. 57-62, 東京, 2017年3月. <br>
        <div class="mybtn3"><a href="http://www.ieice.org/ken/paper/201703076bSz/">paper</a></div>
    </div>

    <div class="papercard">
        <strong>経験損失最小化問題における高速感度分析に関する一提案</strong> <br>
        <u>花田博幸, <i>柴垣篤志</i>, 佐久間淳, 竹内一郎</u> <br>
        信学技報, vol. 116, no. 209, <a href="http://ibisml.org/ibisml026">IBISML</a> 2016-35, pp. 203-210, 富山, 2016年9月. <br>
        <div class="mybtn3"><a href="http://www.ieice.org/ken/paper/20160906Xbkj/">paper</a></div>
    </div>

    <div class="papercard">
        <strong>スパースモデルのための特徴と標本の同時セーフスクリーニング</strong> <br>
        <u><i>柴垣篤志</i>, 烏山昌幸, 畑埜晃平, 竹内一郎</u> <br>
        信学技報, vol. 116, no. 121, <a href="http://ibisml.org/ibisml025">IBISML</a> 2016-4, pp. 201-208, 沖縄, 2016年7月. <br>
        <div class="mybtn3"><a href="http://www.ieice.org/ken/paper/20160706YbjI/">paper</a></div>
    </div>

    <div class="papercard">
        <strong>L2正則化凸損失関数最小化問題のための検証誤差近似保証付きモデル選択</strong><br>
        <u><i>柴垣篤志</i>, 鈴木良規, 竹内一郎</u> <br>
        信学技報, vol. 114, no. 502, <a href="http://ibisml.org/ibisml020">IBISML</a> 2014-96, pp. 79-86, 京都, 2015年3月.<br>
        <div class="mybtn3"><a href="http://www.ieice.org/ken/paper/20150306DBZ8/">paper</a></div>
    </div>

Preprint
^^^^^^^^^^
.. raw:: html

    <div class="menu">
        <label for="Panel3">
        <strong>Efficiently Bounding Optimal Solutions after Small Data Modification in Large-Scale Empirical Risk Minimization</strong> <br>
        <u>H. Hanada, <i>A. Shibagaki</i>, J. Sakuma, and I. Takeuchi</u> <br>
        <div class="mybtn3"><a href="http://arxiv.org/abs/1606.00136">arXiv:1606.00136</a></div>
        </label>
        <input type="checkbox" id="Panel3" class="on-off"/>
        <ul> <div class="abst"> <b>Abstract: </b>
        We study large-scale classification problems in changing environments where a small part of the dataset is modified, and the effect of the data modification must be quickly incorporated into the classifier. When the entire dataset is large, even if the amount of the data modification is fairly small, the computational cost of re-training the classifier would be prohibitively large. In this paper, we propose a novel method for efficiently incorporating such a data modification effect into the classifier without actually re-training it. The proposed method provides bounds on the unknown optimal classifier with the cost only proportional to the size of the data modification. We demonstrate through numerical experiments that the proposed method provides sufficiently tight bounds with negligible computational costs, especially when a small part of the dataset is modified in a large-scale classification problem. </div> </ul> <br>
    </div>


Activities
^^^^^^^^^^^^^
.. rst-class:: actli

    - **Dec (2016):**
      Poster presentation in `情報系 WINTER FESTA Episode2 <http://bigdata.nii.ac.jp/johokei-winterfesta2/program>`_ @ Tokyo

    - **Nov (2016):**
      Poster presentation in `IBIS2016 <http://ibisml.org/ibis2016/poster1/>`_ @ Kyoto Univ.

    - **Mar (2015):**
      Oral presentation in `IBISML25 <http://ibisml.org/ibisml025>`_ @ Okinawa.

    - **Jun (2016):**
      Poster presentation in `ICML 2016 <http://icml.cc/2016/>`_ @ New York City

    - **Dec (2015):**
      Poster presentation in `NIPS 2015 <https://nips.cc/Conferences/2015>`_ @ Montreal

    - **Nov (2015):**
      Poster presentation in `IBIS2015 <http://ibisml.org/ibis2015/poster1/>`_ @ Tsukuba

    - **Aug - Sep (2015):**
      Poster presentation in `Machine Learning Summer School (MLSS) 2015 <http://www.iip.ist.i.kyoto-u.ac.jp/mlss15/doku.php/>`_ @ Kyoto Univ.

    - **Mar (2015):**
      Got bachelor's degree form Nagoya Institute of Technology (Department of Computer Science)
      **Award:** `電影会賞 <http://www.denei.jp/news/1427331600.html>`_

    - **Mar (2015):**
      Oral presentation in `IBISML20 <http://ibisml.org/ibisml020>`_ @ Kyoto Univ.




Memo
^^^^^

.. toctree::
   :maxdepth: 1

   misc_memo
   git_memo
   tex_memo

.. Memo
.. -------

.. * :doc:`misc_memo`
.. * :doc:`git_memo`
.. * :doc:`tex_memo`

..     - **Mar (2017):**
..      Got master's degree form Nagoya Institute of Technology (Department of Scientific and Engineering Simulation)

