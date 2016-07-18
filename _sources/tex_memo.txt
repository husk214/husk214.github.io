# TeX

## algorithm2e
```
\begin{algorithm}
\DontPrintSemicolon
\SetKwData{Left}{left}\SetKwData{This}{this}\SetKwData{Up}{up}
\SetKwFunction{Union}{Union}\SetKwFunction{FindCompress}{FindCompress}
\SetKwInOut{Input}{input}\SetKwInOut{Output}{output}
\Input{$w_0 \in \dom P_{\lambda} , \alpha_0 \in \dom D_{\lambda} $}
% \Output{$x$}
\BlankLine
\For{$t = 1,2,\ldots$ \KwTo converged}{
  \If{Broadly working set algortm}{
    $(w^{(t-1)}, \alpha^{(t-1)} ) \lA U^{(1)}(w^{(t-1)}, \alpha^{(t-1)}) $ \;
  }
  $(\cF^{(t)}, \cS^{(t)}) \lA (\cW_{\cF} (w^{(t-1)} ), \cW_{\cS} (\alpha^{(t-1)} ))$ \;
  $(\hat{w}^{(0)}, \hat{\alpha}^{(0)} ) \leftarrow ({w}^{(t-1)} , {\alpha}^{(t-1)} )$\;
  \For{$ u = 1,2, \ldots$ \KwTo until satisfy $C(\hat{w}^{(u)}, \hat{\alpha}^{(u)} ) $}{
    $(\hat{w}^{(u)}, \hat{\alpha}^{(u)} ) \lA U^{(2)}(\hat{w}^{(u-1)}, \hat{\alpha}^{(u-1)}) $ \;
  }
  \uIf{Broadly working set algortm and $G_\lambda (\hat{w}^{(u)}, \hat{\alpha}^{(u)} ) > G_\lambda ({w}^{(t-1)}, {\alpha}^{(t-1)} )$}{
    $({w}^{(t)}, {\alpha}^{(t)} ) \lA ({w}^{(t-1)}, {\alpha}^{(t-1)} )$\;
  }
  \uElse{
    $({w}^{(t)}, {\alpha}^{(t)} ) \lA (\hat{w}^{(u)}, \hat{\alpha}^{(u)} )$\;
  }
}
\caption{Strictly and Broadly Working Set Algorithm (Primal-Dual)}\label{alg:ws}
\end{algorithm}
```

## document template

```
\documentclass[a4paper,10pt]{ltjsarticle}

\usepackage{hyperref}
\usepackage{xltxtra}
\usepackage{xunicode}
% \usepackage{fontspec}
% \usepackage{luatexja-fontspec}

\usepackage{amsmath,amssymb}
\usepackage{amsthm}
% \usepackage{algorithmic,algorithm}
\usepackage[ruled,vlined]{algorithm2e}
\usepackage{graphicx}
\usepackage{color}
\usepackage{atbegshi}
\usepackage{ulem}
\usepackage{mathbbol}
\usepackage{braket}
\usepackage{subfig}
\usepackage[yyyymmdd]{datetime}

\usepackage{/Users/Shibagaki/GoogleDrive/Tex/mcr}
\usepackage{/Users/Shibagaki/GoogleDrive/Tex/mycolor}

\makeatletter
\def\@maketitle{
\begin{center}
{\LARGE \@title \par}
\end{center}
\begin{flushright}
{\large \@date}
\end{flushright}
\begin{flushright}
{\large \@author}
\end{flushright}
\par\vskip 1.5em
}
\makeatother
\title{Material}
\date{\today}
\author{Atsushi Shibagaki}

\begin{document}
\maketitle

\end{document}
```

## beamer template

```
% \documentclass[11pt,notheorems,pdflatex]{beamer}
\documentclass[11pt,notheorems,lualatex]{beamer}
% \usepackage{luatexja}
\usepackage{hyperref}
\usepackage{xltxtra}
\usepackage{xunicode}
\usepackage{fontspec}
\usepackage{luatexja-fontspec}

\usepackage{amsmath,amssymb}
\usepackage{amsthm}
\usepackage{algorithmic,algorithm}
\usepackage{graphicx}
\usepackage{color}
\usepackage{atbegshi}
\usepackage{ulem}
\usepackage{mathbbol}
\usepackage{braket}

\usepackage{/Users/Shibagaki/GoogleDrive/Tex/mcr}
\usepackage{/Users/Shibagaki/GoogleDrive/Tex/mycolor}
\usepackage{/Users/Shibagaki/GoogleDrive/Tex/mybeamer2}

% \usefonttheme{professionalfonts}

\hypersetup{unicode=true}
\setmainfont[Ligatures=TeX]{Helvetica neue}
\setsansfont[Ligatures=TeX]{Helvetica neue}

\setmainjfont[BoldFont=IPAexGothic]{IPAexGothic}
\setsansjfont{IPAexGothic}
\newjfontfamily\jisninety[CJKShape=JIS1990]{IPAexGothic}

% \AtBeginSection[]
% {
%   \begin{frame}<beamer>
%     \frametitle{Outline for section \thesection}
%     \tableofcontents[currentsection]
%   \end{frame}
% }

\title[tit]
      {Title}
\author[Shibagaki]{Atsushi Shibagaki}
\institute[Nitech]{Nagoya Institute of Technology}
\date{\today}
\begin{document}

\begin{frame}[plain] \frametitle{}
\titlepage
\end{frame}
```
