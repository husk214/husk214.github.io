# blog

# how to build

## init

```
pip install sphinx myst-parser myst-nb sphinxcontrib-pseudocode 
pip install pandas scipy numba matplotlib tensorflow torch
```

(tensorflow, torch等を使ったnotebookがあるため)

reference: http://uokada.hatenablog.jp/entry/2018/05/28/005924

## build

```
cd origin
sphinx-build -nW --keep-going -b html . html
```

## mv　(bashで実行)
```
cd origin
cp -r -f html/* ../
(windows powershell) cp -r -Force html/* ../
```
