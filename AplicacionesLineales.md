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

## Matriz de una aplicación lineal asociada

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