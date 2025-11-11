# Aplicaciones Lineales

:::{prf:definition} Aplicación lineal
:label: app_lineal
Llamaremos aplicación lineal a una función $f:U\to V$, donde $U$ y $V$ son dos espacios vectoriales sobre el mismo cuerpo de escalares $\mathbb{K}$, que cumple:
- Para todo $\mathbf{u}_1$ y $\mathbf{u}_2$ de $U$ se tiene que $f(\mathbf{u}_1+\mathbf{u}_2)=f(\mathbf{u}_1)+f(\mathbf{u}_2)$.
- Para todo $k\in\mathbb{K}$ y todo $\mathbf{u}\in U$ se tiene que $f(k\mathbf{u})=kf(\mathbf{u})$.
:::

:::{note}
:class: dropdown
Dependiendo del autor, a una aplicación lineal también se la puede llamar **homomorfismo lineal** o simplemente **homomorfismo**, pues en términos generales, un homomorfismo es una aplicación entre dos estructuras del mismo tipo, que conserva la forma de dicha estructura. Así un homomorfismo *lineal* es lo mismo que un homorfismo entre espacios vectoriales, y como la propiedad que define a un espacio vectorial es que cualquier conmbinación lineal de sus elementos sea otro elemento del espacio, una homomorfismo lineal es aquél en el que la aplicación de la función a una combinación lineal de vectores es lo mismo que la combinación lineal de imágenes de dichos vectores.

Si, por ejemplo, estuviésemos hablando de [grupos](#grupo), un homomorfismo de grupos, u homomorfismo entre grupos, sería una función $f:(G,*)\to(H,\times)$ que cumple que $f(a*b)=f(a)\times f(b)$.

Por ejemplo la función $f(x)=e^x$ es un homomorfismo entre el grupo $(\mathbb{R},+)$ y $(\mathbb{R}^*,\cdot)$, pues 
$$
f(x+y)=e^{x+y}=e^xe^y=f(x)f(y)
$$
:::

::::{prf:property}
Una condición necesaria para que una aplicación $f:U\to V$ sea lineal, es que $f(\mathbf{0}_U)=\mathbf{0}_V$, donde $\mathbf{0}_U$ y $\mathbf{0}_V$ denotan los vectores nulos de $U$ y $V$ respectivamente.
:::{prf:proof}
:class:dropdown
:enumerated: false
Simplemente teniendo en cuenta que $0\in\mathbb{K}$, y teniendo en cuenta que $f(k\mathbf{u})=kf(\mathbf{u})$ tenemos que 
$$
f(\mathbf{0}_U)=f(0\mathbf{u})=0f(\mathbf{u})=\mathbf{0}_V
$$
donde $\mathbf{u}$ es un vector cualquiera de $U$.
:::
::::

:::{prf:example} Coordenadas
Como ya dijimos el isomorfismo de coordenadas es una aplicación lineal. Si $U=\mathcal{M}_2(\mathbb{R})$ y $V=\mathbb{R}^4$ y definimos la base de $U$ como
$$
\mathcal{B}_U = \left\{\begin{bmatrix}1 & 0 \\ 0 & 0 \end{bmatrix}, \begin{bmatrix}0 & 1 \\ 0 & 0 \end{bmatrix}, \begin{bmatrix}0 & 0 \\ 1 & 0 \end{bmatrix}, \begin{bmatrix}0 & 0 \\ 0 & 1 \end{bmatrix}\right\}
$$
Tenemos que las coordenadas de la matriz nula: 
$$
\mathbf{0}_U = \begin{bmatrix}0 & 0 \\ 0 & 0\end{bmatrix}
$$
son justamente $\mathbf{0}_V=(0,0,0,0)$.

:::


:::{prf:example} Rotación
Consideramos la aplicación $f:\mathbb{R}^2\to\mathbb{R}^2$ definida como:
$$
f(x,y)=(-y,x)
$$
:::

:::{prf:example} Proyección
Consideramos la aplicación $f:\mathbb{R}^2\to\mathbb{R}^2$ definida como:
$$
f(x,y)=(x,0)
$$

:::

:::{prf:example} Derivación
Consideramos la aplicación $f:\mathbb{R}_2[t]\to\mathbb{R}_2[t]$ definida como:
$$
f(a_0 + a_1t + a_2t^2) = a_1 + 2a_2t
$$
:::


:::{prf:definition} Núcleo de una aplicación lineal
:label: kernel
Definimos el núcleo o kernel de una aplicación lineal $f:U\to V$, como el subconjunto de $U$ dado por:
$$
\ker f = \{\mathbf{u}\in U \,|\, f(\mathbf{u}) = \mathbf{0}\}
$$
:::

::::{prf:property}
El núcleo de una aplicación lineal es un subespacio vectorial del dominio.
:::{prf:proof}
:enumerated: False
:class: dropdown

Dados $\mathbf{u}_1, \mathbf{u}_2\in\ker f$ y dados $\alpha,\beta\in\mathbb{K}$, queremos probar que $\alpha \mathbf{u}_1 + \beta \mathbf{u}_2$ también pertenece a $\ker f$. 

Para que $\alpha \mathbf{u}_1 + \beta \mathbf{u}_2$ pertenezca al núcleo lo que se tiene que cumplir es que $f(\alpha \mathbf{u}_1 + \beta \mathbf{u}_2)=\mathbf{0}$. Por ser $f$ una aplicación lineal se tiene que:
$$
f(\alpha \mathbf{u}_1 + \beta \mathbf{u}_2)=\alpha f(\mathbf{u}_1) + \beta f(\mathbf{u}_2)
$$
Ahora bien, por pertenecer $\mathbf{u}_1$ y $\mathbf{u}_2$ al núcleo de $f$ tenemos que $f(\mathbf{u}_1)=\mathbf{0}$ y $f(\mathbf{u}_2)=\mathbf{0}$, por lo que:
$$
f(\alpha \mathbf{u}_1 + \beta \mathbf{u}_2)=\alpha \mathbf{0} + \beta \mathbf{0} = \mathbf{0}
$$
que es lo que queríamos demostrar.
:::
::::

:::{prf:definition} Imagen de una aplicación lineal
:label: imagen
Definimos la imagen de una aplicación lineal $f:U\to V$, como el subconjunto de $V$ dado por:
$$
\mathrm{Im} f = \{\mathbf{v}\in V \,|\, \mathbf{v} = f(\mathbf{u}) \;\text{para algún}\;\mathbf{u}\in U\}
$$
:::

::::{prf:property}
La imagen de una aplicación lineal es un subespacio vectorial del codominio.
:::{prf:proof}
:enumerated: False
:class: dropdown
Dada una aplicación lineal $f:U\to V$ queremos demostrar que dados $\mathbf{v}_1,\mathbf{v}_2$ pertenecientes a $\mathrm{Im}f$ se tiene que $\alpha \mathbf{v}_1 + \beta \mathbf{v}_2$ también pertenece a $\mathrm{Im} f$, esto es, que existe un vector $\mathbf{u}\in U$ tal que $f(\mathbf{u})=\alpha \mathbf{v}_1 + \beta \mathbf{v}_2$.

Por una parte, por pertenecer $\mathbf{v}_1$ a la imagen de $f$, entonces existe $\mathbf{u}_1\in U$ tal que $f(\mathbf{u}_1)=\mathbf{v}_1$. Del mismo modo existe $\mathbf{u}_2\in U$ tal que $f(\mathbf{u}_2)=\mathbf{v}_2$. 

Por ser $U$ un espacio vectorial, existe un vector $\mathbf{u}\in U$ tal que $\mathbf{u}=\alpha \mathbf{u}_1 + \beta \mathbf{u}_2$. Además, por ser $f$ lineal se tiene que:

$$
f(\mathbf{u})=f(\alpha \mathbf{u}_1 + \beta \mathbf{u}_2)=\alpha f( \mathbf{u}_1) + \beta f(\mathbf{u}_2)=\alpha \mathbf{v}_1 + \beta \mathbf{v}_2
$$
Por lo que acabamos de demostrar que $\alpha \mathbf{v}_1 + \beta \mathbf{v}_2$ pertenece a la imagen de $f$.

:::
::::

:::{prf:definition} Rango de una aplicación lineal
:label: rango_app
Llamamos rango de una aplicación lineal a la dimensión de la imagen de la aplicación lineal.
:::

::::{prf:theorem} Rango-nulidad
Dada una aplicación lineal $f:U\to V$ entre espacios vectoriales de dimensión finita, se tiene que: 
$$
\mathrm{dim}(U)=\mathrm{dim}(\ker f) + \mathrm{dim}(\mathrm{Im}f)
$$
::::

## Matriz asociada a una aplicación lineal

Supongamos que tenemos una aplicación lineal $f:U\to V$ y tenemos una base $\mathcal{B}_U=\{\mathbf{u}_1,\mathbf{u}_2,\dots,\mathbf{u}_n\}$ de $U$, y otra $\mathcal{B}_V=\{\mathbf{v}_1,\mathbf{v}_2,\dots,\mathbf{v}_m\}$ de $V$. Si conociésemos el valor de $f(\mathbf{u}_1)$ automáticamente podríamos conocer el valor de $f(\mathbf{u})$ para cualquier $\mathbf{u}\in\mathscr{L}(\{\mathbf{u}_1\})$, pues $\mathbf{u}=k\mathbf{u}_1$ así que

$$
f(\mathbf{u})=f(k\mathbf{u}_1)=kf(\mathbf{u}_1)
$$
donde nos acabamos de aprovechar de que $f$ es [lineal](#app_lineal).

Del mismo modo, si conociésemos las imágenes por $f$ de cada uno de los vectores de $\mathcal{B}_U$, es decir, si conociésemos $\{f(\mathbf{u}_1),f(\mathbf{u}_2),\dots, f(\mathbf{u}_n)\}$, ya podríamos conocer la imagen por $f$ de cualquier vector $\mathbf{u}\in U$, pues:

$$
f(\mathbf{u})=f((x_1,x_2,\dots, x_n)_{\mathcal{B}_U}) = \sum_{i=1}^n x_i f(\mathbf{u}_i)
$$
donde $(x_1,x_2,\dots, x_n)$ son las coordenadas del vector $\mathbf{u}$ en la base $\mathcal{B}_U$.



:::{prf:example} Derivación
:label: ex_deriv
Vamos a calcular la matriz asociada a la aplicación $f:\mathbb{R}_2[t]\to\mathbb{R}_1[t]$ tal que 
$$
f(p(t)) = p'(t)
$$

Es decir es aquella aplicación que al polinomio $a_0 + a_1t + a_2t^2$ le asigna el polinomio $a_1 + 2a_2t$.

Las bases usuales de los espacios vectoriales de polinomios en este caso son $\{1,t,t^2\}$ y $\{1,t\}$, por lo que la matriz asociada a la aplicación lineal en dichas bases es: 

$$
A=\begin{bmatrix}
0 & 1 & 0 \\
0 & 0 & 2 \\
\end{bmatrix}
$$

Así, por ejemplo, si queremos calcular la derivada del polinomio $p(t) = 3 + 4t + 5t^2$, cuyas coordenadas en la base usual son $(3,4,5)$, escribirlas como una matriz columna y multiplicar por $A$:

$$
\begin{bmatrix}
4 \\
10
\end{bmatrix}
=
\begin{bmatrix}
0 & 1 & 0 \\
0 & 0 & 2 \\
\end{bmatrix}
\begin{bmatrix}
3 \\ 
4 \\ 
5
\end{bmatrix}
$$

De donde obtenemos que el polinomio derivada de $p$ tiene coordenadas $(4,10)$ en la base usual, es decir $p'(t)=4 + 10t$.
:::


### Cambio de base de la matriz asociada a una aplicación lineal

Supongamos que tenemos una aplicación $f:U\to V$, siendo $U$ y $V$ espacios vectoriales de dimensión $n$ y $m$ respectivamente. Una vez que definimos unas bases $\mathcal{B}_U$ y $\mathcal{B}_V$ podemos calcular la matriz $A\in\mathscr{M}_{m\times n}(\mathbb{K})$ asociada a dicha aplicación en esas bases. Recordamos que la matriz $A$ cumple que $Y=AX$ donde si $X$ denota a la matriz columna formada por las coordenadas de un vector $\mathbf{u}\in U$ en la base $\mathcal{B}_U$, entonces $Y$ denota a la matriz columna formada por las coordenadas del vector $f(\mathbf{u})$ en $\mathcal{B}_V$.


:::{prf:definition} Equivalencia de matrices
:label: linealmente_equivalente
Dadas dos matrices $A,B\in\mathscr{M}_{m\times n}(\mathbb{K})$, decimos que $A$ y $B$ son linealmente equivalentes si existen las [matrices regulares](#matriz_regular) $P\in\mathscr{M}_n(\mathbb{K})$ y $Q\in\mathscr{M}_m(\mathbb{K})$ tales que:

$$
B = Q^{-1}AP
$$

Dicho de otra manera, $A$ y $B$ son matrices asociadas a la misma aplicación lineal en bases diferentes.
:::

:::{prf:example}
Como ya comentamos en el [](#ex_deriv), la matriz asociada la derivación de polinomios de segundo grado en las bases usuales es: 

$$
A = \begin{bmatrix}
0 & 1 & 0 \\
0 & 0 & 2 \\
\end{bmatrix}
$$

Vamos a calcular cual sería la matriz $A'$ asociada a dicha aplicación lineal en las bases $\mathcal{B}_2=\{1-t^2, t^2 - t, t^2 + t\}$ y $\mathcal{B}_1=\{t,1-t\}$.

Por una parte, la matriz de cambio de la base $\mathcal{B}_2$ a la base usual de $\mathbb{R}_2[t]$ es: 

$$
P = 
\begin{bmatrix}
 1 & 0 & 0\\
 0 &-1 & 1\\
-1 & 1 & 1
\end{bmatrix}
$$

y por otra parte la matriz de cambio de $\mathcal{B}_1$ a la base usual de $\mathbb{R}_1[t]$ es:

$$
Q = \begin{bmatrix}
0 & 1 \\
1 & -1 
\end{bmatrix}
$$

Para calcular $A'$ necesitamos $Q^{-1}$, que es la matriz que cambia de la base usual de $\mathbb{R}_1[t]$ a $\mathcal{B}_1$, asi que calculamos la inversa mediante el método de Gauss:

$$
\begin{bmatrix}
0 & 1 & 1 & 0 \\
1 & -1 & 0 & 1 
\end{bmatrix}
$$
intercambiando filas $1$ y $2$:
$$
\begin{bmatrix}
1 & -1 & 0 & 1 \\ 
0 & 1 & 1 & 0 
\end{bmatrix}
$$

y sumando la fila $2$ a la fila $1$:

$$
\begin{bmatrix}
1 & 0 & 1 & 1 \\
0 & 1 & 1 & 0 
\end{bmatrix}
$$
con lo que la inversa es:

$$
Q^{-1}=
\begin{bmatrix}
 1 & 1 \\
 1 & 0 
\end{bmatrix}
$$

Finalmente, para calcular la matriz $A'=Q^{-1}AP$ realizamos el producto de matrices:

$$
\begin{align}
A' =& \begin{bmatrix}
 1 & 1 \\
 1 & 0 
\end{bmatrix}\begin{bmatrix}
0 & 1 & 0 \\
0 & 0 & 2 \\
\end{bmatrix}\begin{bmatrix}
 1 & 0 & 0\\
 0 &-1 & 1\\
-1 & 1 & 1
\end{bmatrix} \\
 =& \begin{bmatrix}
 1 & 1 \\
 1 & 0 
\end{bmatrix}\begin{bmatrix}
0 & -1 & 1 \\
-2 & 2 & 2 \\
\end{bmatrix}\\
=&\begin{bmatrix}
-2 & 1 & 3 \\
0 & -1 & 1 \\
\end{bmatrix}
\end{align}
$$

Para comprobar que la calculamos correctamente basta con verificar que las derivadas de los vectores de la base $\mathcal{B}_2$ coinciden con las columnas de la matriz $A'$ cuando las escribimos en la base $\mathcal{B}_1$:

La derivada de $1 - t^2$ es $-2t=(-2,0)_{\mathcal{B}_1}$, la derivada de $(t^2 - t)$ es $2t-1=-(1-t)+t=(1,-1)_{\mathcal{B}_1}$  y por último la derivada de $t^2+t$ es $2t+1=(1-t)+3t=(3,1)_{\mathcal{B}_1}$, con lo que queda comprobado.
:::

::::{prf:example} Matriz de una rotación:
Como ya comentamos en el ejemplo BLA, la matriz de una rotación antihoraria de ángulo $\theta$ cuando se usa la base canónica es: 

$$
A=\begin{bmatrix}
\cos\theta & -\sin\theta \\
\sin\theta & \cos\theta 
\end{bmatrix}
$$ 


Vamos a calcular la matriz $A'$ asociada a la aplicación lineal cuando decidimos usar como base $\mathcal{B}'=\{(1,-1),(1,1)\}$. 

:::{figure} 
:alt: Dos flechas a 45 grados.
Dibujo de las flechas asociadas a la base $\mathcal{B}'$.
:::

Puesto que estamos utilizando las mismas bases tanto para $U$ como para $V$, realmente solo tenemos una matriz de cambio de base, $P$, y la relación entre $A'$ y $A$ será $A'=P^{-1}AP$, donde:

$$
P=\begin{bmatrix}
1 & 1 \\
-1 & 1
\end{bmatrix}, \quad 
P^{-1}=\begin{bmatrix}
\frac{1}{2} & -\frac{1}{2} \\
\frac{1}{2} &  \frac{1}{2} 
\end{bmatrix}
$$

Por lo tanto podemos calcular $A'$ como:

$$
\begin{align}
A'=& \begin{bmatrix}
\frac{1}{2} & -\frac{1}{2} \\
\frac{1}{2} &  \frac{1}{2} 
\end{bmatrix} \begin{bmatrix}
\cos\theta & -\sin\theta \\
\sin\theta & \cos\theta 
\end{bmatrix}\begin{bmatrix}
1 & 1 \\
-1 & 1
\end{bmatrix}\\
=&\begin{bmatrix}
\frac{1}{2} & -\frac{1}{2} \\
\frac{1}{2} &  \frac{1}{2} 
\end{bmatrix} \begin{bmatrix}
\cos\theta +\sin\theta & \cos\theta - \sin\theta \\
\sin\theta -\cos\theta & \sin\theta + \cos\theta 
\end{bmatrix}\\
=&\begin{bmatrix}
\cos\theta & -\sin\theta \\
\sin\theta & \cos\theta
\end{bmatrix}
\end{align}
$$

Es decir, en este caso se cumple que $A'=A$. ¿Por qué?, Pues porque una rotación de un ángulo $\theta$ sigue siendo una rotación de un ángulo $\theta$ la miremos desde el ángulo que la miremos.
::::

:::{prf:definition} Monomorfismo
Decimos que una aplicación lineal $f:U\to V$ es un monomorfismo si es [inyectiva](#f_inyectiva) es decir, si para cualquier par de vectores $\mathbf{x},\mathbf{y}\in U$ se tiene que $\mathbf{x}\neq\mathbf{y}$ implica que $f(\mathbf{x})\neq f(\mathbf{y})$.
:::

::::{prf:property} 
Una aplicación lineal $f$ es un monomorfismo si y solo si $\ker f = \{\mathbf{0}\}$, o lo que es lo mismo, una aplicación lineal es un monomorfismo si y solo si $\mathrm{dim}\left(\ker f\right) = 0$.
:::{prf:proof}
:enumerated: false
:class: dropdown
Vamos a demostrar primero que si $f$ es un monomorfismo, entonces el kernel tiene que ser únicamente el vector $\mathbf{0}$ mediante el recíproco. Supongamos que la consecuencia es falsa, es decir, que existe un vector $\mathbf{v}\neq \mathbf{0}$ que pertenece al kernel de $f$. En ese caso se tiene tenemos que $f(\mathbf{0})=\mathbf{0}=f(\mathbf{v})$, por lo que acabamos de encontrar dos vectores distintos $\mathbf{0}$ y $\mathbf{v}$ para los cuales la aplicación toma el mismo valor, por lo que no se trataría de un monomorfismo.

Por otra parte si el kernel es únicamente el vector $\mathbf{0}$, la aplicación ha de ser un monoformismo, pues si no fuese un monomorfismo existirían al menos dos vectores distintos $\mathbf{x}$ e $\mathbf{y}$ tales que $f(\mathbf{x})=f(\mathbf{y})$, y en ese caso tendríamos que el vector $\mathbf{y}-\mathbf{x}$ cumpliría $f(\mathbf{x}-\mathbf{y})=f(\mathbf{x})-f(\mathbf{y})=\mathbf{0}$. Es decir, el vector $\mathbf{x}-\mathbf{y}$ sería un vector distinto de $\mathbf{0}$ y perteneciente al kernel de $f$, lo cual va en contra de que el kernel de $f$ sea únicamente el vector $\mathbf{0}$.
:::
::::

:::{prf:definition} Epimorfismo
Decimos que una aplicación lineal $f:U\to V$ es un epimorfismo si es [sobreyectiva](#f_sobreyectiva) es decir, si para cualquier vector $\mathbf{y}\in V$ existe al menos un vector $\mathbf{x}\in U$ tal que $f(\mathbf{x})=\mathbf{y}$. O dicho de otra manera, la [imagen](imagen) de $f$ es todo el espacio vectorial $V$. 
:::

:::{prf:definition} Isomorfismo
Decimos que una aplicación lineal $f:U\to V$ es un isomorfismo si es [biyectiva](#f_biyectiva) es decir, si es tanto un monomorfismo como un epimorfismo.
:::