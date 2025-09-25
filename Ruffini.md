# Método de Ruffini

El método de Ruffini sirve para encontrar o comprobar si un valor $\alpha$ es raíz de un polinomio $p(x)$ y además nos aporta directamente la factorización de dicho polinomio $p(x) = q(x)(x-\alpha)$.

Supongamos que tenemos un polinomio con coefficientes enteros 
$$
p(x) = a_n x^n + a_{n-1}x^{n-x}+\dots +a_1x+a_0
$$
y que $\alpha$ es una raíz de dicho polinomio, entonces se tiene que $p(x)=q(x)(x-\alpha)$ siendo 
$$
q(x) = b_{n-1}x^{n-x}+\dots +b_1x+b_0
$$ 
un polinomio de grado $n-1$, es decir:
$$
 a_n x^n + a_{n-1}x^{n-x}+\dots +a_1x+a_0 = \left(b_{n-1}x^{n-x}+\dots +b_1x+b_0\right)(x-\alpha)
$$
de donde se deduce que $a_0=-b_0\alpha$, pues es el único producto que puede tener grado $0$. Esto tiene una consecuencia muy importante, si un polinomio de coeficientes enteros admite raíces enteras, entonces el coeficiente de orden $0$ tiene que ser divisible por cada una de ellas.

Entonces, una metodología a seguir podría consistir en probar, sistemáticamente, todos los divisores enteros del coeficiente de orden $0$. Por ejemplo para el polinomio 
$$
p(x)=x^3 -3x^2 - x + 3
$$ 
probaríamos con los divisores enteros de $3$, es decir $\{-3,-1,1,3\}$:

- $x=-3$:

$$
p(-3)=(-3)^3 -3(-3)^2 -(-3) + 3 = -27-27+3+3=-48\neq 0
$$

- $x=-1$:

$$
p(-1)=(-1)^3 -3(-1)^2 -(-1) + 3 = -1-3+1+3=0
$$

- $x=1$:

$$
p(1)=(1)^3 -3(1)^2 -(1) + 3 = 1-3-1+3=0
$$

- $x=3$:

$$
p(3)=(3)^3 -3(3)^2 -(3) + 3 = 27-27-3+3=0
$$

Con lo que ya encontramos las tres raíces del polinomio, y por lo tanto podemos asegurar que:

$$
x^3 -3x^2 - x + 3 = (x-3)(x-1)(x+1)
$$

Vamos a probar con otro polinomio:

$$
p(x) = x^3 - 5x^2 + 7x  -3
$$

De nuevo únicamente debemos probar con cualquiera de los valores $\{-3,-1,1,3\}$:

- $x=-3$:

$$
p(-3)=(-3)^3 -5(-3)^2 +7(-3) - 3 = -27 -45 - 21 - 3 < 0 \neq 0
$$

- $x=-1$:

$$
p(-1)=(-1)^3 -5(-1)^2 +7(-1) - 3 = -1 -5 - 7 - 3 < 0 \neq 0
$$

- $x=1$:

$$
p(1)=(1)^3 -5(1)^2 +7(1) - 3 = 1 -5 + 7 - 3 = 0
$$

- $x=3$:

$$
p(3)=(3)^3 -5(3)^2 +7(3) - 3 = 27 -45 + 21 - 3 = 0
$$

Por lo que únicamente encontramos dos raíces, $x=1$ y $x=3$. Esto significa que 

$$
x^3 - 5x^2 + 7x  -3 = (ax+b)(x-1)(x-3)
$$
con $a$ y $b$ desconocidos. Por lo tanto necesariamente tiene que existir otra raíz que no fuimos capaces de calcular todavía. Vamos a ver qué pasa si dividimos el polinomio original por $x-1$

$$
\begin{align*}
&x^3&   &-5x^2& + &7x&  -&3& | &\underline{x - 1} \\
&x^3&  &-x^2&    &&     &&      &x^2  \\
 &0&    &-4x^2&  + &7x&  -&3&
\end{align*}
$$

$$
\begin{align*}
&x^3&   &-5x^2& + &7x&  -&3& | &\underline{x - 1} \\
&x^3&  &-x^2&    &&     &&      &x^2  -4x\\
 &0&    &-4x^2&  + &7x&  -&3& \\
 &&    &-4x^2&  + &4x&  && \\
  &&    &0&  + &3x&  -&3&
\end{align*}
$$

$$
\begin{align*}
&x^3&   &-5x^2& + &7x&  -&3& | &\underline{x - 1} \\
&x^3&  &-x^2&    &&     &&      &x^2  -4x + 3\\
 &0&    &-4x^2&  + &7x&  -&3& \\
 &&    &-4x^2&  + &4x&  && \\
  &&    &&   &3x&  -&3& \\
  &&    &&   &3x&  -&3& \\
  &&    &&   &0&  &0& \\
\end{align*}
$$

Es decir, que el polinomio original se puede factorizar como:
$$
x^3 - 5x^2 + 7x  -3 = (x^2 -4x + 3)(x-1)
$$

De los cálculos anteriores sabemos que $x=3$ tiene que ser una raíz de $x^2 -4x + 3$ y es sencillo comprobar que lo es, pero es que resulta que $x=1$ también lo es. Por lo tanto la factorización del polinomio original es

$$
x^3 - 5x^2 + 7x  -3 = (x-3)(x-1)^2
$$
y sus tres raíces son $x=1$ doble y $x=3$.

El método de Ruffini no hace otra cosa que calcular de golpe, si un valor $\alpha$ es raíz del polinomio y a su vez, el cociente entre el polinomio y $x-\alpha$, de manera que se puede utilizar iterativamente para encontrar todas las raíces enteras, aunque se trate de raíces dobles.