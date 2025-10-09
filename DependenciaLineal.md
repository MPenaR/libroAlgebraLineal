# Dependencia lineal

:::{prf:definition} Dependencia lineal
Dados dos vectores $\mathbf{u}$ y $\mathbf{v}$ decimos que $\mathbf{v}$ depende linealmente de $\mathbf{u}$ si existe un escalar $k\in\mathbb{K}$ tal que $\mathbf{v}=l\mathbf{u}$.
:::

Es sencillo comprobar que el vector nulo depende linealmente de cualquier vector $\mathbf{u}\in V$, pues $\mathbf{0}=0\mathbf{u}$ y que ningún vector distinto del $\mathbf{0}$ depende linealmente del $\mathbf{0}$. 

::::{prf:property} 
En el conjunto $V\setminus \{\mathbf{0}\}$, la dependencia lineal es una propiedad simétrica, es decir, $\mathbf{u}\neq\mathbf{0}$ depende linealmente de $\mathbf{v}\neq\mathbf{0}$ si y solo si $\mathbf{v}\neq\mathbf{0}$ depende linealmente de $\mathbf{u}\neq\mathbf{0}$.

:::{prf:proof}
:class: dropdown
Basta con tomar $k'=\frac{1}{k}$ en la definición de dependencia lineal, pues si ambos son distintos de $\mathbf{0}$, entonces $k$ no puede ser $0$.

::::

:::{prf:definition} Combinación lineal
Dado  un conjunto de vectores $S=\left\{\mathbf{u}_1, \mathbf{u}_n, \dots, \mathbf{u}_n\right\}$, decimos que $\mathbf{v}$ es combiación lineal de los vectores de $S$, o que depende linealmente de los vectores de $S$, si existen $n$ escalares $\alpha_1,\alpha_2,\dots, \alpha_n$ tales que:

$$
\mathbf{v} = \sum_{i=1}^n \alpha_i \mathbf{u}_i = \alpha_1 \mathbf{u}_1 + \alpha_2 \mathbf{u}_2 + \dots + \alpha_n \mathbf{u}_n
$$
:::

:::{prf:definition} Sistema linealmente dependiente
Decimos que un conjunto de vectores $S=\left\{\mathbf{u}_1, \mathbf{u}_n, \dots, \mathbf{u}_n\right\}$ si existe alguno de ellos que sea combinación lineal del resto de vectores. 
:::

::::{prf:criterion}
:enumerated: false

Un conjunto de vectores $S=\left\{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n\right\}$ es linealmente dependiente sí y solo sí existen $n$ escalares $\alpha_1, \alpha_2,\dots, \alpha_n$, no todos ellos cero, tal que:
$$
\alpha_1 \mathbf{u}_1 + \alpha_2 \mathbf{u}_2 + \dots + \alpha_n \mathbf{u}_n = \mathbf{0}
$$
:::{prf:proof}
:class: dropdown
Tenemos que probar la doble implicación. Por una parte si $S$ es un sistema linealmente dependiente, entonces existe al menos un vector que se puede escribir como combinación lineal de los demás. Supongamos que dicho vector es el $\mathbf{u}_1$, por comodidad, pues si fuese otro la demostración sería completamente análoga. Por ser combinación lineal, entonces existen $n-1$ escalares $\beta_2, \beta_3, \dots, \beta_n$, tales que:

$$
\mathbf{u}_1 = \beta_2\mathbf{u}_2 + \beta_3\mathbf{u}_3 + \dots + \beta_n\mathbf{u}_n 
$$

Por lo tanto, restando $\mathbf{u}_1$ a ambos lados tenemos que:

$$
\mathbf{0} = - \mathbf{u}_1 +  \beta_2\mathbf{u}_2 + \beta_3\mathbf{u}_3 + \dots + \beta_n\mathbf{u}_n 
$$

con lo que llamando $\alpha_1 = - 1$ y $\alpha_n = \beta_n$ para $n=2,3,\dots, n$, tenemos que 

$$
\mathbf{0} = \alpha_1\mathbf{u}_1 +  \alpha_2\mathbf{u}_2 + \dots + \beta_n\mathbf{u}_n 
$$
que es lo que queríamos demostrar. 

Por otra parte, si existen $n$ escalares $\alpha_1, \alpha_2,\dots, \alpha_n$, no todos ellos cero, tal que:
$$
\alpha_1 \mathbf{u}_1 + \alpha_2 \mathbf{u}_2 + \dots + \alpha_n \mathbf{u}_n = \mathbf{0}
$$

entonces podemos escoger uno de ellos que sea distinto de $0$. Vamos a suponer, otra vez, sin pérdida de generalidad, que el $\alpha_1$ es distinto de $0$. Si dividimos toda la ecuación anterior por $-\alpha_1$ tenemos que 

$$
- \mathbf{u}_1 + \frac{\alpha_2}{-\alpha_1} \mathbf{u}_2 + \dots + \frac{\alpha_n}{-\alpha_1} \mathbf{u}_n = \mathbf{0}
$$

Por lo que sumando $\mathbf{u}_1$ a ambos lados obtenemos que:

$$
\mathbf{u}_1 = \left(- \frac{\alpha_2}{\alpha_1}\right) \mathbf{u}_2 +\left(- \frac{\alpha_3}{\alpha_1}\right) \mathbf{u}_3 + \dots + \left(- \frac{\alpha_n}{\alpha_1}\right) \mathbf{u}_n
$$

es decir, que $\mathbf{u}_1$ es combinación lineal del resto de vectores de $S$.
:::
::::

## Espacio generado por un conjunto de vectores

::::{prf:property} 
Dado un espacio vectorial $V$ y un subconjunto de vectores $S=\left\{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n\right\}$ de $V$, el conjunto $U$ formado por todo aquel vector de $V$ que se puede escribir como combinación lineal de vectores de $S$ es un subespacio vectorial de $S$ es un subespacio vectorial de $V$. 

:::{prf:proof}
:enumerated: false
:class: dropdown

Sean $\mathbf{v}$ y $\mathbf{w}$ dos vectores que se pueden escribir como combinación lineal de vectores de $S$. Entonces existen $n$ escalares $\alpha_1, \alpha_2, \dots, \alpha_n$ y otros $n$ escalares $\beta_1, \beta_2, \dots, \beta_n$ tales que:

$$
\mathbf{v} = \alpha_1\mathbf{u}_1 + \alpha_2\mathbf{u}_2 + \dots \alpha_n\mathbf{u}_n 
$$
$$
\mathbf{w} = \beta_1\mathbf{u}_1 + \beta_2\mathbf{u}_2 + \dots \beta_n\mathbf{u}_n 
$$

Si ahora construimos una combinación lineal de dichos vectores, $\lambda\mathbf{v}+\mu\mathbf{w}$obtenemos que:

$$
\lambda\mathbf{v}+\mu\mathbf{w} = \left(\lambda\alpha_1+\mu\beta_1\right)\mathbf{u}_1 + \left(\lambda\alpha_2+\mu\beta_2\right)\mathbf{u}_2 + \dots \left(\lambda\alpha_n+\mu\beta_n\right)\mathbf{u}_n
$$
con lo que definiendo $\gamma_i = \lambda\alpha_i+\mu\beta_i$ desde $i=1$ hasta $n$, se tiene que 
$$
\lambda\mathbf{v}+\mu\mathbf{w} = \gamma_1\mathbf{u}_1 + \gamma_2\mathbf{u}_2 + \dots \gamma_n\mathbf{u}_n 
$$
:::

::::

Al espacio vectorial formado por las combinaciones lineales de elementos de $S$ lo denotamos por $\mathscr{L}(S)$ y decimos que $\mathscr{L}(S)$ está generado por $S$. 

:::{prf:definition} Sistema generador
Dado un espacio vectorial $V$ y un subespacio vectorial $U$ decimos que el subconjunto $S$ de $V$ es un sistema generador de $U$ si $U=\mathscr{L}(S)$. 
:::

Otra forma de definir al espacio $\mathscr{L}(S)$ es el menor de los subespacios vectoriales que contiene a $S$, entendiendo _menor_ en el sentido de la inclusión.

::::{prf:property} 
Todo subespacio vectorial $U$ que contenga a $S$ contiene también a $\mathscr{L}(S)$. 

:::{prf:proof}
:enumerated: false
:class: dropdown

Si $U$ es un espacio vectorial, entonces contiene a cualquier combinación lineal de sus elementos. Como $S$ está contenido en $U$, entonces $U$ contiene en particular a cualquier combinación lineal de los vectores de $S$, por lo tanto contiene a cualquier elemento de $\mathscr{L}(S)$.
:::
::::

:::{prf:example}
Dado el espacio vectorial $V=\mathbb{R}^3$, el conjunto $S=\{(1,1,0)\}$ y el subespacio vectorial

$$
U = \left\{(x,y,0);\,x,y\in\mathbb{R}^2\right\}
$$

Es sencillo comprobar que $U$ contiene a todo vector del conjunto $S$, pues el único elemento del conjunto es el vector $(1,1,0)$, que se puede obtener con $x=y=1$ en la definición de $U$.

Por otra parte, $\mathscr{L}(S)=\mathscr{L}(\{(1,1,0)\})=\{(\lambda,\lambda,0);\, \lambda\in\mathbb{R}\}$, y dicho espacio también está contenido en $U$ pues basta hacer $x=y$ en la definición de $U$. Sin embargo $U$ contiene vectores que no están en $\mathscr{L}(S)$ como por ejemplo el vector $(1,2,0)$.
:::


:::{prf:definition} Espacio finitamente generado
Decimos que un espacio vectorial es finitamente generado si existe un conjunto finito $S$ de vectores de $U$ tal que $U=\mathscr{L}(S)$. 
:::

:::{prf:example} Espacio vectorial de polinomios
Hasta ahora consideramos los espacios vectoriales de los polinomios de grado menor o igual que $n$ para cierto $n\in\mathbb{N}$ fijo. También podemos considerar el espacio vectorial $V=\mathbb{R}[x]$, formado por todos los polinomios, de cualquier grado. Es fácil demostrar que dicho espacio no es finitamente generado. 

Supongamos que fuese un espacio finitamente generado, entonces existiría un subconjunto de polinomios $S$, finito, tal que $V=\mathscr{L}(S)$. Como $S$ es finito existirá al menos uno de los polinomios cuyo grado será mayor o igual que el resto de los polinomios de $S$. Llamando $m$ al grado de dicho polinomio, tenemos que cualquier combinación lineal de elementos de $S$ será un polinomio de grado menor o igual que $m$, pues el grado de un polinomio no aumenta ni al sumarlo a otros polinomios de su mismo grado ni al multiplicarlo por un número real. 

Por lo tanto tendríamos que el polinomio $p(x)=x^{m+1}$ sería un elemento de $V$ que no pertenece a $\mathscr{L}(S)$, por lo que no es cierto que $S$ sea un sistema generador de $V$. 

Como podemos aplicar dicha demostración a cualquier sistema generador con un número finito de elementos acabamos de demostrar que $V$ no es un espacio finitamente generado.
:::

Dicho esto, en esta asignatura únicamente se estudiarán espacios vectoriales finitamente generados.

## Bases de un espacio vectorial

Supongamos que tenemos un sistema $S=\{\mathbf{u}_1,\mathbf{u}_2,\dots,\mathbf{u}_n\}$ que genera un espacio $U$ de manera que el mismo vector $\mathbf{v}$ se puede escribir mediante dos combinaciones lineales diferentes de los vectores de $S$, es decir que existen dos conjuntos de $n$ escalares $\{\alpha_i\}$ y $\{\beta_i\}$ tales que:

$$
\mathbf{v}=\alpha_1\mathbf{u}_1 + \alpha_2\mathbf{u}_2 + \dots + \alpha_n\mathbf{u}_n = \beta_1\mathbf{u}_1 + \beta_2\mathbf{u}_2 + \dots + \beta_n\mathbf{u}_n 
$$
y de modo que para algún $i$ entre $1$ y $n$ se tiene que $alpha_i\neq \beta_i$. La igualdad anterior se puede escribir como  

$$
\left(\alpha_1 - \beta_1\right)\mathbf{u}_1 + \left(\alpha_2 - \beta_2\right)\mathbf{u}_2 + \dots + \left(\alpha_n - \beta_n\right)\mathbf{u}_n  = \mathbf{0}
$$

y llamando $\gamma_i = \alpha_i - \beta_i$ acabamos de encontrar un conjunto de $n$ escalares $\{\gamma_i\}$, no todos ellos nulos, tales que:

$$
\gamma_1\mathbf{u}_1 + \gamma_2\mathbf{u}_2 + \dots + \gamma_n\mathbf{u}_n = \mathbf{0}
$$
por lo que acabamos de demostrar que si existen dos combinaciones lineales distintas que generan el mismo vector, entonces el sistema es linealmente dependiente.

Del mismo modo, si el sistema fuese linealmente dependiente, existiría un vector que se podría escribir como combinación lineal de los demás, y por lo tanto cualquier vector perteneciente a $U$ se podría expresar mediante combinaciones lineales de $S$ diferentes.

Es interesante por lo tanto tratar los sistemas generadores linealmente independientes.

:::{prf:definition} Base de un espacio vectorial
Dado un conjunto ordenado $S$, decimos que $S$ es una base del espacio vectorial $U$ si: 
- $S$ es un sistema generador de $U$.
- $S$ es un sistema de vectores linealmente independiente.
:::

:::{prf:example} Base usual de los polinomios
Sea $V=\mathbb{R}_2[x]$ el espacio vectorial de los polinomios de grado menor o igual que $2$. Cualquier elemento de $V$ será de la forma $p(x) = a_0 + a_1 x + a_2 x^2 $, por lo que el conjunto $\mathcal{B}=\{1,x,x^2\}$ es un sistema generador de $V$. 

Además el sistema es linealmente independiente, pues podemos comprobar que si existiesen tres escalares $a,b,c$ tales que el polinomio
$$
p(x)= a + bx + cx^2 
$$
fuese igual al polinomio $0$, entonces tendríamos que $a=0$, $b=0$ y $c=0$. 

Por lo tanto el sistema $B$ es una base de $V$, y se le conoce como base usual de los polinomios de grado menor o igual que $2$.

Existen más bases para el mismo espacio, por ejemplo el sistema $\mathcal{B}'={1-x^2, x^2 - x, x^2 + x}$ también es una base de $V$. 

:::



::::{prf:property} 
Dado un espacio vectorial $(V,+.)$ sobre un cuerpo $\mathbb{K}$ finitamente generado, toda base de dicho espacio tiene el mismo número de elementos.
:::{prf:proof}
:enumerated: False
:class:dropdown

Supongamos que tenemos dos bases $\mathcal{B}$ y $\mathcal{B}'$ de un mismo espacio vectorial $V$ y que $\mathcal{B}'$ tiene más elementos que $B$.

::::


