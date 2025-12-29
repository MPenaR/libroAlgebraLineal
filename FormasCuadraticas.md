# Formas cuadráticas

:::{prf:definition} Forma cuadrática
Dado un espacio vectorial $V$, llamamos forma cuadrática, a una aplicación $\omega:V\to \mathbb{R}$ que cumple que, para todo $\lambda\in\mathbb{R}$ y para todo $\mathbf{v}\in V$ se tiene que $\omega(\lambda \mathbf{v})=\lambda^2\mathbf{v}$.
:::

:::{prf:definition} Forma polar
Dada una forma cuadrática $\omega: V\to \mathbb{K}$, llamamos forma polar de $\omega$ a la aplicación bilineal $f:V\times V \to \mathbb{R}$ definida como
$$
f(\mathbf{x},\mathbf{y})=\frac{\omega(\mathbf{x}+\mathbf{y}) - \omega(\mathbf{x}) - \omega(\mathbf{y})}{2}
$$
:::

::::{prf:property}
La forma polar de una forma cuadrática es una forma bilineal simétrica.
:::{prf:proof}
:enumerated: false
:class: dropdown

\begin{align}
f(\mathbf{y},\mathbf{x}) &= \frac{\omega(\mathbf{y}+\mathbf{x}) - \omega(\mathbf{y}) - \omega(\mathbf{x})}{2} \\
                         &= \frac{\omega(\mathbf{x}+\mathbf{y}) - \omega(\mathbf{x}) - \omega(\mathbf{y})}{2} \\
                         &= f(\mathbf{x},\mathbf{y})
\end{align}
:::
::::

Llamamamos matriz asociada a la forma cuadrática $\omega$ en la base $\mathcal{B}$ a la matriz asociada a la forma polar en dicha base. O dicho de otra manera, dada una base $\mathcal{B}$, la matriz asociada a una forma cuadrática $\omega$ es la única matriz simétrica $A$ que cumple que:

$$
\omega(\mathbf{x})=X^\intercal A X
$$
siendo $X$ la matriz columna formada por las coordenadas de $\mathbf{x}$ en la base $\mathcal{B}$.

::::{prf:property}
Toda forma cuadrática admite una base en la que la matriz asociadad es diagonal
:::{prf:proof}
:enumerated: false
:class: dropdown

La matriz asociada a una forma cuadrática es simétrica y sabemos que toda matriz simétrica es diagonalizable por semejanza, por lo que en una base $\mathcal{B}$ ortonormal formada por autovectores de $A$, la matriz asociadada será:

$$
D = P^{-1}AP  = \begin{pmatrix}
\lambda_1 & 0 & \dots & 0 \\
0 & \lambda_2 & \ddots & \vdots \\
\vdots & \ddots & \ddots & 0 \\
0 & \dots & 0 & \lambda_k 
\end{pmatrix}
$$

Y puesto que la base es ortonormal, $P^{-1}=P^\intercal$, por lo que
$$
A' = P^\intercal A P = P^{-1}AP = D
$$
será la matriz asociada a la forma $\omega$ en la base $\mathcal{B}$.
::::


::::{prf:theorem} Ley de inercia de Sylvester
Sean $A$ y $B$ dos matrices simétricas de tamaño $n$ y sea $P$ una matriz regular de tamaño $n$ tal que $B=P^\intercal A P$. Entonces $A$ y $B$ poseen el mismo número de autovalores positivos y el mismo número de autovalores negativos.
::::


::::{prf:property}
Si $P$ es una matriz cuadrada, entonces $A=P^\intercal P$ es una matriz simétrica semidefinida positiva. Si además $P$ es regular, entonces $A$ es definida positiva. 

:::{prf:proof}
:enumerated: False
:class: dropdown

A es simétrica pues $A^\intercal=(P^\intercal P)^\intercal=P^\intercal {P^\intercal}^\intercal=P^\intercal P = A$ y es definida positiva pues 
$$
X^\intercal A X = X^\intercal P^\intercal P X = (PX)^\intercal PX = (P\mathbf{x})\cdot(P\mathbf{x}) = \|P\mathbf{x}\|^2\ge0
$$
Si además $P$ es regular, entonces $\ker P = \{\mathbf{0}\}$ y por lo tanto 
$$
X^\intercal A X = 0 \Rightarrow \|P\mathbf{x}\|=0 \Rightarrow P\mathbf{x}=\mathbf{0} \Rightarrow \mathbf{x}=\mathbf{0}
$$
por lo que $A$ es definida positiva.
:::
::::


## Diagonalización de formas cuadráticas

Toda matriz simétrica $2\times 2$ es diagonalizable pues si suponemos que

$$
A = \begin{pmatrix}
a & b \\
b & c
\end{pmatrix}
$$
tenemos que su polinomio característico es: 
$$
p(\lambda)=\vert A - \lambda I\vert = \begin{vmatrix}
a-\lambda & b \\
b & c-\lambda
\end{vmatrix} = \lambda^2  - (a+c)\lambda + ac - b^2 
$$
y sus raíces vienen dadas por la fórmula para la solución de las ecuaciones de segundo grado:
$$
\lambda = \frac{a+b\pm\sqrt{(a+c)^2 -4ac + 4b^2}}{2}=\frac{a+b\pm\sqrt{(a-c)^2  + 4b^2}}{2}
$$
como se puede comprobar, o bien existen dos raíces reales distintas, o bien existe una raíz real doble.

Si existen dos raíces reales distintas, $\lambda_1$ y $\lambda_2$, entonces existen dos autovectores $\mathbf{u}_1$ y $\mathbf{u}_2$, asociados a dichos autovalores, y por lo tanto en la base $\mathcal{B}=\left\{\mathbf{u}_1,\mathbf{u}_2\right\}$ la matriz $A'=P^{-1}AP$ es diagonal. 

Por otra parte, si únicamente existe un autovalor $\mu$ doble, para que sea diagonalizable tenemos que ser capaces de encontrar dos autovectores linealmente independientes asociados a $\mu$. Supongamos que llamamos $\mathbf{u}$ a uno de ellos (que tiene que existir) y cuya norma es $1$. Vamos a $\mathbf{v}$ a un vector perteneciente a $\mathbf{u}^\perp$ y cuya norma sea $1$. Esto podemos hacerlo por Gram-Schmidt. 

En la base $\mathbf{B}=\left\{\mathbf{u},\mathbf{v}\right\}$, la matriz $A'$ será de la forma:

$$
A'=\begin{pmatrix}
\mu & \alpha \\
0 & \mu 
\end{pmatrix}
$$
pues sabemos que la primera columna tiene que ser $(\mu,0)$ por ser $f(\mathbf{u})=\mu \mathbf{u}$ y además el polinomio característico tiene que ser $p(\lambda)=(\lambda - \mu)^2$. 

Por otra parte, puesto que $\mathcal{B}$ es una base ortonormal, sabemos que $P^\intercal P = I$. Por lo que 

$$
A'=P^\intercal A P
$$

y si $A$ era simétrica, $A'$ tiene que serlo. Con esto concluimos que 
$$
A'=\begin{pmatrix}
\mu & 0 \\
0 & \mu 
\end{pmatrix}
$$
que efectivamente es diagonal, con lo que $\mathbf{v}$ es también un autovector de $A$. 

Este último resultado, que los subespacios propios sean ortogonales, es algo que se cumplirá en cualquier matriz simétrica.

::::{prf:property} 
Los [subespacios propios](#subespacio_propio) de una matriz simétrica son [subespacios ortogonales](#subs_ortogonales) con respecto al producto escalar usual.
:::{prf:proof}
:class: dropdown
:enumerated: false

Si $A$ es simétrica se tiene que $A=A^\intercal$, por lo que 

$$
X^{\intercal}A^\intercal Y - X^\intercal A Y = 0,\quad \forall X,Y\in \mathbb{R}^n
$$

Supongamos ahora que $X\in V_\lambda$ e $Y\in V_\mu$ con $\lambda \neq \mu$. Entonces tenemos:

\begin{align}
0 &= X^{\intercal}A^\intercal Y - X^\intercal A Y \\
  &= (AX)^\intercal Y - X^\intercal (AY) \\
  &=  (\lambda X)^\intercal Y - X^\intercal (\mu Y)\\
  &= \lambda X^\intercal Y - \mu X^\intercal Y \\
  &= (\lambda - \mu)X^\intercal Y\\
  &= X^\intercal Y\\
  &= \mathbf{x}\cdot\mathbf{y}
\end{align}
:::
::::
