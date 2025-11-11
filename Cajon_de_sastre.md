# Definiciones varias

En esta sección solo se incluyen definiciones de temas externos a álgebra que son necesarios durante alguna parte del curso.


:::{prf:definition} Par ordenado
:label: par_ordenado
Llamamos par ordenado o dupla a un conjunto ordenado formado por dos elementos, llamados componentes del par. 

Al par cuya primera componente es $a$ y la segunda es $b$ lo denotamos por $(a,b)$.
:::

Es decir, $(1,2)$ y $(2,1)$ son pares ordenados distintos, mientras que el conjunto $\{1,2\}$ y el conjunto $\{2,1\}$ son el mismo conjunto.

:::{prf:definition} Producto cartesiano
:label: producto_cartesiano
Dados dos conjuntos $A$ y $B$, llamamos producto cartesiano de $A$ y $B$, al conjunto de [pares ordenados](#par_ordenado) cuya primera componente pertenece a $A$ y la segunda componente pertenece a $B$. Lo denotamos por:

$$
A\times B := \{(a,b) \,|\, a \in A,\, b\in B\}
$$
:::

Volvemos a recalcar que se trata de pares **ordenados**, es decir, si $A=\{a,b,c\}$ y $B=\{1,2\}$ tendríamos que $(b,1)$ pertenece a $A\times B$ mientras que $(1,b)$ no.

:::{prf:definition} Tupla
Llamamos tupla, o mas explícitamente $n$-tupla, a un conjunto ordenado formado por $n$ elementos. Del mismo modo que ocurría con los [pares ordenados](#par_ordenado), cada uno de los elementos del conjunto se conoce como componente, pudiéndose hablar de la primera componente, segunda componente, etc...
:::

:::{prf:definition} $\mathbb{R}^n$
:label: R_n
Denotamos por $\mathbb{R}^n$ al conjunto formado por las $n$-tuplas cuyas componentes son números reales.
:::

:::{prf:definition} Función biyectiva
:label: f_biyectiva
:enumerated: false
Decimos que una función es biyectiva cuando es [inyectiva](#f_inyectiva) y [sobreyectiva](#f_sobreyectiva). Si una función $f:A\to B$ es biyectiva entonces existe una función inversa $f^{-1}B\to A$ tal que $f^{-1}f(x)=x$ para todo $x\in A$  y $f(f^{-1}(y))=y$ para todo $y\in B$.
:::


:::{prf:definition} Función inyectiva
:label: f_inyectiva
:enumerated: false
Decimos que una función $f:A\to B$ es inyectiva cuando para cada par $x,y\in A$ se cumple que $x\neq y \Rightarrow f(x)\neq f(y)$.
:::

:::{prf:definition} Función sobreyectiva
:label: f_sobreyectiva
:enumerated: false
Decimos que una función $f:A\to B$ es sobreyectiva si para todo $y\in B$ existe $x\in A$ tal que $f(x)=y$.
:::

:::{prf:definition} Matriz regular
:label: matriz_regular
Decimos que una matriz cuadrada es regular si $\det(A)\neq 0$
:::

:::{prf:definition} Matriz singular
:label: matriz_singular
Decimos que una matriz cuadrada es singular si $\det(A)= 0$
:::