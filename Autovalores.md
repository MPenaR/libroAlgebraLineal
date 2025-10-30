# Endomorfismos lineales

:::{prf:definition} Endomorfismo lineal
:label: endomorfismo

Llamamos endomorfismo lineal a una aplicación lineal $f:U\to U$, es decir, una aplicación lineal entre cuyo dominio y codominio son el mismo espacio vectorial.
:::


### Cambio de base la matriz asociada a un endomorfismo

Si llamamos $P$ a la matriz de cambio de base de coordenadas en la base $\mathcal{B}'$ a coordenadas en la base $\mathcal{B}$, entonces, la matriz $A'$ asociada a un endomorfismo $f$ se pude calcular como $A'=P^{-1}AP$.

:::{prf:definition} Semejanza de matrices
Decimos que dos matrices $A$ y $B$ cuadradas de tamaño $n$ son semejantes si existe una matriz cuadrada $P$ de tamaño $n$, regular, tal que 

$$
B = P^{-1}AP
$$
:::

En otras palabras, dos matrices son semejantes si son matrices asociadas al mismo endomorfismo en bases diferentes.
