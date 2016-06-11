# TeX

## document template

```
\documentclass[a4paper,10pt]{ltjsarticle}

\usepackage{hyperref}
\usepackage{xltxtra}
\usepackage{xunicode}
\usepackage{fontspec}
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
