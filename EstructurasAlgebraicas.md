# Estructuras algebraicas

:::{prf:definition} Grupo
:label: grupo
Llamamos grupo a una estructura algebraica $(G,*)$ formada por un conjunto $G$ y una operación $*:G\times G \to G$ que cumple:
- **Asociatividad:** Para todo $a,b,c\in G$ se tiene que $(a*b)*c=a*(b*c)$.
- **Existencia de elemento neutro:** Existe un elemento $e\in G$ que cumple $e*a=a$ y $a*e=a$ para todo $a\in G$.
- **Existencia de elemento inverso:** Para todo $a\in G$ existe otro elemento $b\in G$ que llamamos inverso de $a$ y cumple $a*b=e$ y $b*a=e$.
- 
:::

:::{prf:example} El grupo de $(\mathbb{Z},+)$
:label: grupo
Los números enteros forman un grupo con la operación de suma pues:
- La suma es asociativa: $(a+b)+c = a+(b+c)$ para cualquier $a$, $b$ y $c$ enteros.
- Existe un elemento, al que llamamos $0$ que cumple que $0+a=a+0=a$ para cualquier $a$ entero.
- Para cada entero $a$ existe otro entero, al que denotamos por $-a$ que cumple que $a + (-a) = 0$. 
:::

::::{prf:property}
El elemento neutro  de un grupo es único y es su propio inverso.
:::{prf:proof}
:enumerated: False
:class:dropdown
Supongamos que existen dos elementos $e_1$ y $e_2$ de $G$ que satisfacen las propiedades de *ser elemento neutro*. Por una parte tenemos que 
$e_1*e_2=e_2$ por ser $e_1$ elemento neutro. Por otra parte tenemos que, como $e_2$ es elemento neutro, entonces $e_1*e_2=e_1$, de donde se deduce que:
$$
e_1=e_1*e_2=e_2
$$
y por lo tanto $e_1=e_2$.

Además tenemos que $e*e=e$ por lo que $e$ es el inverso de $e$. 
:::
::::

:::{prf:definition} Grupo conmutativo
:label: grupo_conmutativo
Decimos que un [grupo](#grupo) $(G.*)$ es conmutativo, o abeliano, si la operación $*$ es conmutativa, es decir, si se cumple que para todo $a$ y $b$ de $G$, se tiene que $a*b=b*a$. 
:::

Por ejemplo el grupo $(\mathbb{Z},+)$ es un grupo abeliano.


:::{prf:definition} Cuerpo
:label: cuerpo
Llamamos cuerpo a una estructura algebraica $(\mathbb{K},+,\times)$ formada por un conjunto y dos operaciones internas.

La operación $+$ la llamaremos *suma* y ha de cumplir:
- **Asociatividad:** Dados $a,b,c\in \mathbb{K}$ entonces $(a+b)+c = a + (b+c)$. 
- **Conmutatividad:** Dados $a,b\in \mathbb{K}$ entonces $a+b=b+a$.
- **Existencia de elemento neutro:** Existe un elemento de $\mathbb{K}$, al que denotamos por $0$, que cumple que $0+a=a$ para todo $a\in \mathbb{K}$.
- **Existencia de elemento opuesto:** Para cada $a\in \mathbb{K}$ existe otro elemento de $\mathbb{K}$, al que denotamos por $-a$ que cumple que $a+(-a)=0$.

En resumen, el conjunto $\mathbb{K}$ ha de ser un [grupo conmutativo](#grupo_conmutativo) con la operación $+$. 

La operación $\times$ la llamaremos *producto* y ha de cumplir:
- **Asociatividad**: Para cada $a,b,c\in\mathbb{K}$ se cumple que $a\times(b\times c) = (a\times b)\times c$.
- **Conmutatividad**: Para cada $a,b\in\mathbb{K}$ se cumple que $a\times b = b \times a$.
- **Existencia de elemento neutro**: Existe un elemento en $\mathbb{K}$, que denotaremos por $1$, que cumple que $1a=a$ para todo $a\in\mathbb{K}$.
- **Existencia de elemento inverso**: Para todo $a\in\mathbb{Z}$ distinto del $\mathbb{0}$ existe otro elemento en $\mathbb{K}$, que denotaremos por $a^{-1}$, que cumple que $a\times a^{-1} = 1$.

Además se tiene que cumplir una relación entre ambas operaciones: 
- **Ditributividad de la suma sobre el producto:** Para cada $a,b,c,\in \mathbb{K}$ se cumple que $a\times (b+c)=a\times b + a \times c $.
:::