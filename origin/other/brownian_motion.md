
# ブラウン運動

## 確率微分方程式

````{prf:definition} 確率微分方程式
:label: def-sde

$x(t)$ が確率微分方程式

$$
 \dd{x} = f(x(t), w(t), t) \dd{t} + g(x(t), w(t), t) \dd{w}
$$

の解であることは、$x$ が

$$
\lim_{\Delta t \rightarrow 0} \Delta x = f(x, w, t) \Delta t + g(x, w, t) \Delta w
$$
の定める確率分布に従う確率変数であること。($\fallingdotseq$ 上の式を満たすこと)

````

````{prf:theorem} 伊藤の公式
:label: ito-formula

$x$ を確率微分方程式
$\dd{x} = f(x, w, t) \dd{t} + g(x, w, t) \dd{w}$
に従う確率過程とする。

このとき、関数 $h=h(x, t)$ の値は次の確率微分方程式

```{math}
\dd{h} = \left( \frac{\partial h}{\partial x} f + \frac{1}{2} \frac{\partial^2 h}{\partial x^2}g^2 \sigma^2 + \frac{\partial h}{\partial t} \right) \dd{t}
  + \frac{\partial h}{\partial x} g \dd{w}
```

に従う。

````




導出: テーラー展開する。

```{math}
\dd{h} 
& = \frac{\partial h}{\partial x} \dd{x} + \frac{\partial h}{\partial t} \dd{t} 
+ \frac{1}{2} \frac{\partial^2 h}{\partial x^2} \dd{x^2} 
+ \frac{\partial^2 h}{\partial x \partial t} \dd{x} \dd{t}
+ \frac{1}{2} \frac{\partial^2 h}{\partial t^2} \dd{t^2}
+ \cdots \\
& ~~ ( \dd{x} = f \dd{t} + g \dd{w} \text{~~を代入すると} ) \\
& = \frac{\partial h}{\partial x} (f \dd{t} + g \dd{w}) + \frac{\partial h}{\partial t} \dd{t} 
+ \frac{1}{2} \frac{\partial^2 h}{\partial x^2} (f \dd{t} + g \dd{w})^2 
+ \frac{\partial^2 h}{\partial x \partial t} (f \dd{t} + g \dd{w}) \dd{t}
+ \frac{1}{2} \frac{\partial^2 h}{\partial t^2} \dd{t^2}
+ \cdots \\


```

この中から$\dd{t}, \dd{w}$の1次の項だけを取りだすことを考える。(1次以降の微小量は極限をとると消えるので)

```{math}
& \frac{\partial h}{\partial x} (f \dd{t} + g \dd{w}) + \frac{\partial h}{\partial t} \dd{t} ~~ \leftarrow \text{この行はそのまま残る} \\
&+ \frac{1}{2} \frac{\partial^2 h}{\partial x^2} (f \dd{t} + g \dd{w})^2 
~ (\leftarrow \frac{1}{2} \frac{\partial^2 h}{\partial x^2} ( \underbrace{f^2 \dd{t}^2}_{\text{消える}} + \underbrace{2fg \dd{t} \dd{w}}_{\dd{w}=\pm \sigma \sqrt{\dd{t}} \text{で1.5次なので消える}} + \underbrace{g^2 \dd{w}^2)}_{ \dd{w}^2 = \sigma^2 \dd{t} \text{なので残る}} )
\\
&+ \frac{\partial^2 h}{\partial x \partial t} (f \dd{t} + g \dd{w}) \dd{t}  ~~ \leftarrow \text{この行は全部消える}  \\
&+ \frac{1}{2} \frac{\partial^2 h}{\partial t^2} \dd{t^2}  ~~ \leftarrow \text{この行は全部消える} \\
&+ \cdots  ~~ \leftarrow \text{これ以降の3次は全部消える}

```

なので

```{math}
\dd{h}
& = \frac{\partial h}{\partial x} (f \dd{t} + g \dd{w}) + \frac{\partial h}{\partial t} \dd{t} + \frac{1}{2} \frac{\partial^2 h}{\partial x^2} g^2  \sigma^2 \dd{t} \\
& = \left( \frac{\partial h}{\partial x} f + \frac{1}{2} \frac{\partial^2 h}{\partial x^2}g^2 \sigma^2 + \frac{\partial h}{\partial t} \right) \dd{t}
  + \frac{\partial h}{\partial x} g \dd{w}
```

が成り立つ。

### ブラック=ショールズ過程

$\dd{x} = ax \dd{t} + bx \dd{w} $ を満たす確率過程

```{math}
\frac{\dd{x}}{x} = ax \dd{t} + bx \dd{w} ~~~ (\text{両辺をxで割る})
```

(左辺のほうはlogになりそうなので) $h(x) = \log x$ とおいて、伊藤の公式を使うと

```{math}
\dd{h}
& = \left( \frac{\partial h}{\partial x} f + \frac{1}{2} \frac{\partial^2 h}{\partial x^2}g^2 \sigma^2 + \frac{\partial h}{\partial t} \right) \dd{t}
  + \frac{\partial h}{\partial x} g \dd{w} \\
& = \left( \frac{1}{x} ax + \frac{1}{2} (-\frac{1}{x^2}) (bx)^2  \sigma^2 + 0  \right) \dd{t} + \frac{1}{x} bx \dd{w} \\
& = \left(a - \frac{1}{2} b^2 \sigma^2 \right) \dd{t} + b \dd{w}   
```

両辺伊藤積分すると

```{math}
\int_0^t \dd{h}
& = \int_0^t \left(a - \frac{1}{2} b^2 \sigma^2 \right) \dd{t} + b \dd{w} \\

\log x(t) - \log x_0 = \left(a - \frac{1}{2} b^2 \sigma^2 \right) t + b w(t) \\

x(t) = x_0 \exp\left( (a - \frac{1}{2} b^2 \sigma^2 ) t + b w(t) \right).
```

平均は増える、中央値はノイズの分だけ減る、

<!-- y = \log S とおいて、 \frac{\partial}{\partial S} = \frac{\partial y}{\partial S} \frac{\partial}{\partial y} = \frac{1}{S} \frac{\partial}{\partial y} -->




## Ref

- AIcia Solid Project [【ブラックショールズ方程式への道④】伊藤の公式【確率微分方程式の基礎】](https://www.youtube.com/watch?v=mrExmReKrcM)