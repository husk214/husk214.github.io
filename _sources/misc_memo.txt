# Misc

## other


### まとめてrename (zshのzmv)

- `zmv 'hoge-(*).(*).(*).tar.gz' 'hoge-$1--$2--$3.tar.gz'`

- `zmv -w 'hoge-*.*.*.tar.gz' 'hoge-$1--$2--$3.tar.gz'`

- `zmv -W 'hoge-*.*.*.tar.gz' 'hoge-*--*--*.tar.gz'`

### 0埋め連番rename

- `(n=1; zmv '*.jpg' '${(l:3::0:)$((n++))}.jpg')`

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
  - .bz2            : `bzip2 target` ( -k: 圧縮及び展開する際，元ファイルを削除しない)
  - .lha .lzh       : `lha c fn.lzh target`
  - .zip            : `zip fn.zip target`

### dmidecode

ハードウエア情報取得

### disown

nohupし忘れ
```
# Ctrl+Zで中断
bg 1
jobs 1
disown %1
```

### top

#### option
  - d 更新間隔(秒)
  - c コマンドのフルパス
  - u 指定したユーザーのプロセスのみ
  - Shift {p, m, t} CPU, メモリ, 実行時間でソート
  - k プロセスIDを指定してkill
  - 1 コア毎に状態を表示

#### status of process
  - S means スリープ
  - T means 停止中
  - D means 割り込み不可(sleep)
  - N means ナイス値がプラスの状態
  - < means ナイス値がマイナスの状態
  - R means 実行中
  - Z means ゾンビ状態
  - W means スワップアウト状態

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
