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



:::{prf:definition} Autovector
Dado un endomorfismo $f:U\to U$ decimos que $\mathbf{v}\in U$ es un autovector de $f$ si $\mathbf{v}\neq \mathbf{0}$ y existe $k\in\mathbb{K}$ tal que $f(\mathbf{v})=k\mathbf{v}$.
:::

:::{prf:definition} Autovalor
Dado un endomorfismo $f:U\to U$ decimos que $\lambda\in\mathbb{K}$ es un autovalor de $f$ asociado al autovector $\mathbf{v}$ si $f(\mathbf{v})=\lambda \mathbf{v}$.
:::

## Cálculo de los autovalores y autovectores de un endomorfismo.

Vamos a ver como podemos calcular los autovalores y autovectores asociados a un endomorfismo. La ecuación que deben de satisfacer es: 

$$
f(\mathbf{v})=\lambda \mathbf{v},\quad \mathbf{v}\neq \mathbf{0}
$$

o lo que es lo mismo

$$
f(\mathbf{v})-\lambda \mathbf{v}=\mathbf{0},\quad \mathbf{v}\neq \mathbf{0}
$$

$$
f(\mathbf{v})-\lambda \mathrm{Id}(\mathbf{v})=\mathbf{0},\quad \mathbf{v}\neq \mathbf{0}
$$
donde $\mathrm{Id}:U\to U$ es la aplicación lineal identidad: $\mathrm{Id}(\mathbf{v})=\mathbf{v}$.

$$
( f - \lambda \mathrm{Id})(\mathbf{v})=\mathbf{0},\quad \mathbf{v}\neq \mathbf{0}
$$

Si $A$ es la matriz asociada al endomorfismo $f$ en la base $\mathcal{B}$, entonces la ecuación anterior se puede reescribir como:

$$
(A - \lambda I)X=\mathbf{0},\quad X\neq \mathbf{0}
$$

El sistema anterior es un sistema homogéneo por lo tanto $X=\mathbf{0}$ será una de sus soluciones. Si queremos que existan mas soluciones entonces necesariamente tendrá que tratarse de un sistema compatible indeterminado, es decir $\mathrm{det}(A-\lambda I)=0$. 

:::{prf:definition} Polinomio característico
Llamamos polinomio característico de un endomorfismo $f:U\to U$ al polinomio:
$$
p(\lambda)= \det(A-\lambda I)
$$
donde $A$ es la matriz asociada al endomorfismo en una base cualquiera de $U$.
:::

::::{prf:property} 
El polinomio característico está bien definido, es decir, no depende de la base $\mathcal{B}$ utilizada.
:::{prf:proof}
:enumerated: false
:class: dropdown
Supongamos que la matriz asociada a un endomorfismo en una base $\mathcal{B}$ es $A$, mientras que en una base $\mathcal{B}'$ es $B=P^{-1}AP$ donde $P$ es la matriz de cambio de base de $\mathcal{B}'$ a $\mathcal{B}$.

Llamando $q(\lambda)$ al polinomio característico que calcularíamos utilizando la base $\mathcal{B}'$ tenemos que:


\begin{align}
q(\lambda) &= \det(B-\lambda I) \\
           &= \det(P^{-1}AP-\lambda I) \\
           &= \det(P^{-1}AP-\lambda P^{-1}P) \\
           &=\det(P^{-1}(A - \lambda I)P)\\
           &=\det(P^{-1})\det(A - \lambda I)\det P\\
           &= \det(A - \lambda I)\\
           &= p(\lambda)
\end{align}
:::
::::