# Espacios vectoriales y subespacios vectoriales

:::{prf:definition} Espacio vectorial
:label: espacio_vectorial
Llamaremos espacio vectorial sobre un [cuerpo](#cuerpo) $\mathbb{K}$ a una terna $(V,+,.)$ donde $V$ es un conjunto cualquiera,  y las operaciones $+$ y $.$ cumplen ciertas propiedades. A los elementos de $V$ los llamaremos _vectores_ del espacio vectorial, mientras que a los elementos de $\mathbb{K}$ los llamaremos _escalares_ del espacio vectorial.

La operación $+$ la llamaremos _suma_ y es una operación binaria interna, es decir $+:V\times V \to V$.

- **Comutatividad**: Para cualquier $\mathbf{u},\mathbf{v}\in V$ se tiene que $\mathbf{u}+\mathbf{v}=\mathbf{v}+\mathbf{u}$
- **Asociatividad**: Para cualquier $\mathbf{u},\mathbf{v},\mathbf{w}\in V$ se tiene que 

$$
\mathbf{u}+(\mathbf{v}+\mathbf{w})=(\mathbf{u}+\mathbf{v})+\mathbf{w}
$$
- **Existencia de elemento neutro**: existe un elemento de $V$ al que denotaremos por $\mathbf{0}$ y llamaremos _cero_ o _nulo_ que cumple que, para cualquier $\mathbf{u}\in V$:

$$
\mathbf{u}+\mathbf{0}=\mathbf{u}
$$
- **Existencia de elemento opuesto**: Para cada elemento $\mathbf{u}\in V$ existirá otro elemento que llamaremos _opuesto_ y denotaremos por $-\mathbf{u}$, que cumple que:

$$
\mathbf{u}+(-\mathbf{u})=\mathbf{0}
$$

Por otra parte, la operación $.$ se llamará _producto por un escalar_ y no es una operación interna, pues toma un elemento de $\mathbb{K}$ y otro de $V$ para devolver un elemento de $V$. Esta cumplirá las siguientes propiedades:

<!-- - **Conmutatividad**: Dados un escalar $\lambda\in\mathbb{K}$ y un vector $\mathbf{u}\in V$, entonces:

$$
\lambda\mathbf{u} = \mathbf{u}\lambda
$$ -->

- **Asociatividad (con respecto al producto de escalares)**: Dados dos escalares $\lambda, \mu \in \mathbb{K}$ y un vector $\mathbf{u}\in V$, entonces se tiene que:

$$
\lambda(\mu \mathbf{u}) = (\lambda \mu) \mathbf{u}
$$

- **Existencia de elemento neutro (escalar)**: Existe un elemento $e$ del cuerpo $\mathbf{K}$ que cumple que $e\mathbf{u}=\mathbf{u}$ para cualquier vector $\mathbf{u}\in V$. Dicho elemento es el elemento neutro del producto del cuerpo $\mathbb{K}$, es decir $e=1$.

- **Propiedad distributiva con respecto a la suma de vectores**: Dados un escalar $\lambda\in \mathbb{K}$ y dos vectores  $\mathbf{u},\mathbf{v}\in V$, entonces:

$$
\lambda(\mathbf{u}+\mathbf{v}) = \lambda\mathbf{u} + \lambda\mathbf{v}
$$

- **Propiedad distributiva con respecto a la suma de escalares**: Dados dos escalares $\lambda,\mu\in \mathbb{K}$ y un vector  $\mathbf{u}\in V$, entonces:

$$
(\lambda+\mu)\mathbf{u} = \lambda\mathbf{u} + \mu\mathbf{u}
$$

:::


En las propedades anteriores estamos haciendo un abuso de la notación. Por ejemplo donde ponemos: 

$$
(\lambda + \mu)\mathbf{u} = \lambda\mathbf{u} + \mu\mathbf{u}
$$

estamos denotando por $+$ primero a la operación que suma dos escalares y luego a la operación que suma dos vectores. En principio esto tendría podría ser un absurdo, pues ambas operaciones en general no serán la misma (pues en general $V$ y $\mathbb{K}$ serán diferentes) y no sabríamos a cual estamos haciendo referencia en cada caso. Sin embargo en estos apuntes seguiremos de manera estricta el convenio de denotar por letras en negrita a los vectores y por letras en fuente normal a los escalares. Así uno puede escribir la expresión anterior reutilizando el símbolo $+$ con dos significados diferentes, en vez de tener que inventar un símbolo nuevo para diferenciar cada operación:

$$
(\lambda \underset{\mathbb{K}}{+} \mu)u = \lambda u  \underset{V}{+} \mu u
$$

Así por ejemplo podemos deducir que la expresión:

$$
\mathbf{u} + \left(\lambda + \mathbf{v}\right)
$$
no está bien definida, pues aparece la expresión $\lambda + \mathbf{v}$ que no hace referencia a ninguna suma conocida, pues estaría sumando un escalar y un vector.

De las propiedades anteriormente mencionadas se pueden deduciar muchas otras.

::::{prf:property} Producto de un escalar por el vector nulo.
Para todo escalar $k$ se tiene que $k\mathbf{0}=\mathbf{0}$.

:::{prf:proof}
:enumerated: false
:class: dropdown

Teniendo en cuenta la propiedad distributiva con respecto a la suma vectorial tenemos que:

$$
\lambda \mathbf{u} = \lambda(\mathbf{u}+\mathbf{0}) = \lambda\mathbf{u}+\lambda \mathbf{0}
$$

Con lo que sumando $-\lambda\mathbf{u}$ a ambos lados obtenemos que:

$$
\mathbf{0}=\lambda \mathbf{0}
$$
:::

::::


::::{prf:property} Producto del escalar cero por cualquier vector.
Para todo vector $\mathbf{u}$ se tiene que $0\mathbf{u}=\mathbf{0}$.

:::{prf:proof}
:enumerated: false
:class: dropdown

Teniendo en cuenta la propiedad distributiva con respecto a la suma escalar tenemos que:

$$
\lambda \mathbf{u} = (\lambda+0)\mathbf{u} = \lambda\mathbf{u}+0 \mathbf{u}
$$

Con lo que sumando $-\lambda\mathbf{u}$ a ambos lados obtenemos que:

$$
\mathbf{0}=0 \mathbf{u}
$$
:::

::::



:::{prf:definition} Espacio vectorial real
Se llama espacio vectorial real a un espacio vectorial sobre el cuerpo de los reales.
:::

:::{prf:definition} Espacio vectorial complejo
Se llama espacio vectorial complejo a un espacio vectorial sobre el cuerpo de los complejos.
:::

En estos apuntes, si alguna propiedad se cumple tanto en espacios vectoriales reales como complejos, hablaremos de espacios vectoriales sobre un cuerpo $\mathbb{K}$ sin especificar el cuerpo del que se trata. Si hablamos de espacio vectorial sin más, se asume que se trata de un espacio vectorial real.

## Ejemplos
:::{prf:example} El espacio vectorial $\mathbb{R}^2$
:label: ej_R2
Podemos definir un espacio vectorial real sobre el conjunto de [pares ordenados reales](#R_n), $\mathbb{R}^2$, definiendo las operaciones suma y producto por un escalar como:

- suma: Dados los pares $\mathbf{u}=(a,b)$ y $\mathbf{v}=(c,d)$ entonces definimos la suma $\mathbf{u}+\mathbf{v}$ como el par $(a+c, b+d)$.
- producto por un escalar: Dado el par $\mathbf{u}=(a,b)$ y el real $\lambda$ entonces definimos el producto $\lambda\mathbf{u}$ como el par $(\lambda a, \lambda b)$.
:::

:::{exercise}
:label: ex_r2
Comprobar que en el [ejemplo %s](#ej_R2) las operaciones definidas cumplen las propiedades de un espacio vectorial.
:::

:::{exercise}
:label: ex_r2_raro
Comprobar que si en el [ejemplo %s](#ej_R2) se hubiese definido la suma como:

$$
(a,b)+(c,d)=(b+d, a+c)
$$
no se trataría de un espacio vectorial
:::

::::{prf:example} Flechas en el plano
:label: ej_flechas
Vamos a definir un espacio vectorial en el conjunto $V$ consistente en todas las flechas que salen de un mismo punto $O$:

:::{figure} flechas_plano.jpg
:width: 60%
Representación gráfica del conjunto $V$.
:::

Por una parte definimos la suma de dos flechas $\mathbf{u}$ y $\mathbf{v}$ como aquella flecha $\mathbf{w}$ que va desde el punto $O$ hasta el punto concidente con la punta de la flecha $\mathbf{v}$ cuando colocamos su final sobre la punta de la flecha $\mathbf{v}$.

:::{figure} suma_flechas.jpg
:width: 60%
Representación gráfica de la suma de flechas.
:::

Por otra parte definimos el producto de un escalar $\lambda$ por una flecha $\mathbf{u} de la siguiente manera:

- Si $\lambda=0$ entonces el resultado es la _flecha nula_ es decir, aquella en la que tanto final como punta coinciden con el punto $O$. 

- Si $\lambda>0$ entonces el resultado es una flecha con la misma dirección y sentido que la flecha $\mathbf{u}$ pero cuya longitud es $\lambda$ veces la longitud de $\mathbf{u}$.

- Si $\lambda<0$ entonces el resultado es una flecha con la misma dirección y sentido opuesto a la flecha $\mathbf{u}$ pero cuya longitud es $|\lambda|$ veces la longitud de $\mathbf{u}$.

:::{figure} flecha_por_escalar.jpg
:width: 60%
Representación gráfica del producto de una flecha por un real.
:::

::::


:::{exercise}
:label: ex_flechas
Probar que el conjunto de flechas con las operaciones definidas en el [ejemplo %s](ej_flechas) constituye un espacio vectorial.
:::

:::{prf:example} Espacios de polinomios
Llamaremos $\mathbb{R}_n[x]$ al conjunto de polinomios de variable real de grado menor o igual que $n$. Es sencillo comprobar que la suma usual polinomios

$$
\begin{align*}
a_0 + a_1x + \dots a_nx^n + b_0+b_1x+\dots b_n x^n =\\
(a_0+b_0) + (a_1+b_1)x + \dots + (a_n+b_n)x^n
\end{align*}
$$

 y el producto de un polinomio por un número real

$$
\lambda (a_0 + a_1x + \dots + a_nx^n) = \lambda a_0 + \lambda a_1x + \dots + \lambda a_nx^n
$$

cumplen las propiedades de un espacio vectorial.
:::

:::{prf:example} Espacios vectoriales de matrices
Dadas dos matrices $A,B\in \mathcal{M}_{m\times n}(\mathbb{K})$ su suma usual y el producto de una matriz por un escalar cumplen las propiedades de espacio vectorial.
:::


Por lo general, cuando podamos sobreentender cual es el cuerpo de escalares y cuales son las operaciones de suma y producto por un escalar, podremos utilizar $V$ para hacer referencia indistintamente al conjunto de vectores como al espacio vectorial en sí. Así por ejemplo podemos hablar del espacio vectorial $\mathbb{R}^2$ o el espacio vectorial $\mathcal{M}_{2\times 3}(\mathbb{R})$ sin necesidad de escribir $(\mathbb{R}^2,+,.)$, etc.


## Subespacios vectoriales

Dado un espacio vectorial $(V,+,.)$ y un subconjunto $U\subset V$ puede darse el caso de que $(U,+,.)$ sea a su vez un espacio vectorial o no. 

Por ejemplo dado el espacio vectorial $V=\mathbb{R}^3$ con la suma y producto por un escalar usuales, definimos dos subconjuntos.

$$
C = \{(x,y,z)\in \mathbb{R}^3\,|\,x = z\}
$$
$$
D = \{(x,y,z)\in \mathbb{R}^3\,|\,y=1\}
$$

Es sencillo comprobar que el conjunto $D$ no es un espacio vectorial con la suma de $\mathbb{R}^3$ pues dados $\mathbf{u}_1=(x_1,1,z_1)\in C$ y $\mathbf{u}_2=(x_2,1,z_2)\in D$ se tiene que

$$
\mathbf{u}_1 + \mathbf{u}_2 = (x_1+x_2,2,z_1+z_2) \notin D
$$

por lo que la suma no es una operación interna (su resultado no es un elemento del propio conjunto).

Por otra parte, el conjunto $C$ sí que forma un espacio vectorial con dichas operaciones, pues por una parte la suma sí que es una operación interna:

$$
(x_1,y_1,x_1)+(x_2,y,x_2) = (x_1+x_2,y,x_1+x_2)\in C
$$

El producto por un escalar también devuelve un elemento de $C$:

$$
\lambda(x,y,x)=(\lambda x, \lambda y, \lambda x ) \in C
$$

y sabemos que ambas operaciones ya cumplían todas las propiedades de un espacio vectorial, pues $\mathbb{R}^3$ lo era.


:::{prf:definition}
:label: subespacio_vectorial

Dado un espacio vectorial $(V,+,.)$ diremos que un subconjunto $U\subset V$ es un subespacio vectorial de $V$ cuando $(U,+,.)$ sea un [espacio vectorial](#espacio_vectorial) con las mismas operaciones suma y producto por un escalar que $V$.
:::

::::{prf:criterion}
Dado un espacio vectorial $(V,+,.)$ sobre $\mathbb{K}$, un subconjunto $C$ de $V$ será subespacio vectorial sí y solo sí para cualquier par de escalares $\alpha,\beta\in\mathbb{K}$ y cualquier par de vectores $\mathbf{u},\mathbf{v}\in C$, se tiene que el vector  $\alpha\mathbf{u}+\beta\mathbf{v}$ pertenece a $C$.
:::{prf:proof}
:enumerated: false
:class: dropdown

Por una parte, haciendo $\alpha=\beta=1$ tenemos que la anterior condición es equivalente a que la suma sea una operación interna, mientras que haciendo $\beta=0$ tenemos que es equivalente a que el producto escalar devuelva un resultado en $C$. 
:::
::::


::::{prf:property}
La intersección de subespacios vectoriales es un subespacio vectorial. 
:::{prf:proof}
:enumerated: false
:class: dropdown
:::

Sean $V$ y $W$ dos subespacios vectoriales de un espacio vectorial $U$. El conjunto $V\cap W$ será un subconjunto de $U$, por lo que queremos probar que tanto la suma de vectores como el producto por un escalar son cerrados en $V\cap W$.

Supongamos dos escalares cualesquiera $\alpha$ y $\beta$ y dos vectores $\mathbf{u}$ y $\mathbf{v}$ pertenecientes a la interseección $V\cap W$. 

Por pertenecer a la intersección, tenemos que ambos vectores pertenecen tanto a $V$ como a $W$. Ahora bien, por ser $V$ un espacio vectorial se tiene que $\alpha\mathbf{u}+\beta\mathbf{v}$ tiene que pertenecer también a $V$. Del mismo modo se demuestra que también tiene que pertenecer a $W$. Por lo tanto, por pertenecer a ambos, se tiene que $\alpha\mathbf{u}+\beta\mathbf{v}$ pertenece a $V\cap W$, por lo que $V\cap W$ es un espacio vectorial.
::::

Sin embargo la unión de dos subespacios vectoriales en general no será un espacio vectorial. 

:::{prf:example}
Sea $U=\mathbb{R^2}$ el espacio vectorial con las operaciones usuales, definimos dos subespacios vectoriales:

$$
V = \{(x,0);\;x\in\mathbb{R}\}
$$
y
$$
W = \{(0,y);\;y\in\mathbb{R}\}
$$

Es sencillo comprobar que tanto $V$ como $W$ son subespacios vectoriales de $V$, y sin embargo, su unión $V\cap W$ no lo es.

Para demostrar que la unión no es un espacio vectorial bastaría con tomar, por ejemplo, los vectores $\mathbf{v}=(1,0)$ y $\mathbf{w}=(0,1)$. Por pertenecer $\mathbf{v}$ a $V$ se tiene que $\mathbf{v}\in V\cup W$. Del mismo modo, por pertenecer $\mathbf{w}$ a $W$ se tiene que $\mathbf{w}\in V \cup W$. Sin embargo $\mathbf{v}+\mathbf{w}=(1,1)$ el cual no pertenece a $V\cup W$.  

:::




## Soluciones
:::{solution} ex_r2
Primero tenemos que comprobar que $(\mathbb{R}^2,+)$ forman un grupo abeliano, es decir: 

- **Conmutatividad:** Sean $\mathbf{x}=(x_1,x_2)$ y $\mathbf{y}=(y_1,y_2)$ dos elementos cualesquiera de $\mathbb{R}^2$ entonces:

\begin{align}
\mathbf{x} + \mathbf{y} &= (x_1,x_2) + (y_1,y_2) \\
                        &= (x_1+y_1, x_2+y_2) \\
                        &= (y_1+x_1, y_2+x_2) \\
                        &= (y_1,y_2) + (x_1+x_2)\\
                        &= \mathbf{y}+\mathbf{x}
\end{align}

- **Asociatividad:** Sean $\mathbf{x}=(x_1,x_2)$, $\mathbf{y}=(y_1,y_2)$ y $\mathbf{z}=(z_1,z_2)$ tres elementos cualesquiera de $\mathbb{R}^2$ entonces:

\begin{align}
(\mathbf{x} + \mathbf{y})+\mathbf{z} &= \left((x_1,x_2) + (y_1,y_2)\right) + (z_1,z_2) \\
                        &= (x_1+y_1, x_2+y_2) + (z_1,z_2) \\
                        &= ((x_1+y_1)+z_1, (x_2+y_2)+z_2) \\
                        &= (x_1+(y_1+z_1), x_2+ (y_2+z_2))\\
                        &= (x_1,x_2) +(y_1+z_1,y_2+z_2)\\
                        &= (x_1,x_2) + \left((y_1,y_2) + (z_1,z_2)\right)\\
                        &= \mathbf{x} + (\mathbf{y}+\mathbf{z})
\end{align}

- **Existencia de elemento neutro:** Sea $\mathbf{x}=(x_1,x_2)$ un elemento cualquiera de $\mathbb{R}^2$, entonces el elemento $\mathbf{0}:=(0,0)$ es el elemento neutro de la suma pues:

\begin{align}
\mathbf{x}+\mathbf{0} &= (x_1,x_2) + (0,0)\\
                      &= (x_1+0,x_2+0) \\
                      &= (x_1,x_2)\\
                      &= \mathbf{x}
\end{align}

- **Existencia de elemento opuesto:** Sea $\mathbf{x}=(x_1,x_2)$ un elemento cualquiera de $\mathbb{R}^2$, entonces el elemento $-\mathbf{x}:=(-x_1,-x_2)$ es el elemento opuesto pues:

\begin{align}
\mathbf{x}+(-\mathbf{x}) &= (x_1,x_2) + (-x_1,-x_2)\\
                      &= (x_1-x_1,x_2-x_2) \\
                      &= (0,0)\\
                      &= \mathbf{0}
\end{align}

A continuación probamos las propiedades del producto por un escalar:

- **Asociatividad mixta:** Sean $\lambda,\mu \in \mathbb{R}$ escalares y sea $\mathbf{x}=(x_1,x_2)$ un elemento cualquiera de $\mathbb{R}^2$, se tiene que:

\begin{align}
\lambda(\mu \mathbf{x}) &= \lambda(\mu(x_1,x_2)) \\
                        &= \lambda(\mu x_1, \mu x_2)\\
                        &= (\lambda \mu x_1, \lambda \mu x_2)\\
                        &= (\lambda\mu)( x_1, x_2)\\
                        &= (\lambda \mu)\mathbf{x}
\end{align}

- **Distributividad sobre la suma de $\mathbb{R}^2$:** Sea $\lambda\in\mathbb{R}$ un escalar cualquiera y sean $\mathbf{x}=(x_1,x_2)$ e $\mathbf{y}=(y_1,y_2)$ dos elementos de $\mathbb{R}^2$ cualesquiera, entonces:

\begin{align}
\lambda(\mathbf{x}+\mathbf{y}) &= \lambda\left((x_1,x_2) + (y_1,y_2)\right) \\
                               &= \lambda ( x_1+y_1,x_2+y_2)\\
                               &= (\lambda(x_1+y_1), \lambda(x_2+y_2))\\
                               &= (\lambda x_1 + \lambda y_1, \lambda x_2 + \lambda y_2)\\
                               &= (\lambda x_1,\lambda x_2) + (\lambda y_1, \lambda y_2)\\
                               &= \lambda(x_1,x_2) + \lambda(y_1,y_2)\\
                               &= \lambda\mathbf{x} + \lambda\mathbf{y}
\end{align}

:::
:::{solution} ex_r2_raro
Vamos a comprobar si dicha suma es una operación asociativa. Sean $\mathbf{x}=(x_1,x_2)$, $\mathbf{y}=(y_1, y_2)$ y $\mathbf{z}=(Z_1,z_2)$ tres elementos cualquiera de $\mathbb{R}^2$, entonces:

\begin{align}
\mathbf{x}+(\mathbf{y}+\mathbf{z}) &= (x_1,x_2)+\left((y_1,y_2)+(z_1,z_2)\right)\\
                                   &= (x_1,x_2)+(y_2+z_2,y_1+z_1)\\
                                   &= (x_2 + y_1 + z_1, x_1 + y_2 + z_2)
\end{align}

mientras que 

\begin{align}
(\mathbf{x}+\mathbf{y})+\mathbf{z} &= \left((x_1,x_2)+(y_1,y_2)\right)+(z_1,z_2)\\ 
                                   &=  (x_2 + y_2, x_1 + y_1) + (z_1,z_2)\\
                                   &=  (x_1 + y_1 + z_2, x_2 + y_2 + z_1)
\end{align}

que son, en general, diferentes, por lo cual no es una operación asociativa.
:::
