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