# Misc

## other

### まとめてrename (zshのzmv)

- `zmv 'hoge-(*).(*).(*).tar.gz' 'hoge-$1--$2--$3.tar.gz'`

- `zmv -w 'hoge-*.*.*.tar.gz' 'hoge-$1--$2--$3.tar.gz'`

- `zmv -W 'hoge-*.*.*.tar.gz' 'hoge-*--*--*.tar.gz'`


### 解凍コマンド
  - .tar.gz .tgz    : `tar -xzvf fn`
  - .tar.bz2 .tbz   : `tar -xjvf fn`
  - .gz             : `gzip -d fn`
  - .bz2            : `bzip2 -d fn`
  - .lha .lzh       : `lha x fn`
  - .zip            : `unzip fn`

### 圧縮コマンド
  - .tar.gz         : `tar -zcvf fn.tar.gz target`
  - .tar.bz2        : `tar -jcvf fn.tar.bz2 target`
  - .gz             : `gzip target`
  - .bz2            : `bzip2 target`
  - .lha .lzh       : `lha c fn.lzh target`
  - .zip            : `zip fn.zip target`

 #### bzip2
  -k: 圧縮及び展開する際，元ファイルを削除しない


### color
`for c in {000..255}; do echo -n "\e[38;5;${c}m $c" ; [ $(($c%16)) -eq 15 ] && echo;done;echo`


## sublime text

### laTeXTools traditionalBuilder.py

```
DEFAULT_COMMAND_LATEXMK = ['latexmk', '-cd', '-e', "$pdflatex = 'lualatex -interaction=nonstopmode -synctex=1 %S %O'", '-f', '-pdf', 'drop.tex']
```

```
DEFAULT_COMMAND_LATEXMK = ["latexmk", "-cd",
                    "-e", "$latex = 'platex %O -interaction=nonstopmode -synctex=1 %S'",
                    "-e", "$biber = 'biber %O --bblencoding=utf8 -u -U --output_safechars %B'",
                    "-e", "$bibtex = 'upbibtex %O %B'",
                    "-e", "$makeindex = 'makeindex %O -o %D %S'",
                    "-e", "$dvipdf = 'dvipdfmx %O -o %D %S'",
                    "-f", "-norc", "-gg", "-pdfdvi"]
```

### for El Captitan
```
  "osx":  {
    // Path used when invoking tex & friends; MUST include $PATH
    "texpath" : "$PATH:/Library/TeX/texbin:/usr/local/bin:/opt/local/bin"
    // Path to PDF viewer, if needed
    // TODO think about it. Also, maybe configure it here!
  },
```

### subl symbolic link
```
ln -s /Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl /usr/local/bin
```


## emacs

### read-only

```
C-x C-r  # open read-only (read only で開く)
C-x C-q  # release read-only (read only を解除)
M-x toggle-read-only # release read-only (read only を解除)
```
