# El producto escalar



El producto escalar usual


forma bilineal...


:::{prf:definition} Producto escalar real
:label: producto_escalar_real
Dado un espacio vectorial real, llamaremos producto escalar a una [forma bilineal](#forma_bilineal), [simétrica](#forma_simetrica) y [definida positiva](#def_positiva).
:::

:::{prf:definition} Producto escalar complejo
Dado un espacio vectorial complejo, llamaremos producto escalar a una [forma sesquilineal](#forma_sesquilineal), [hermítica](#forma_hermitica) y [definida positiva](#def_positiva).
:::


:::{prf:definition} Espacio vectorial euclídeo
:label: espacio_euclideo
Llamaremos espacio vectorial euclídeo a un espacio vectorial en el que hayamos definido un producto escalar.
:::

:::{prf:definition} Norma inducida por un producto escalar
Dado un espacio vectorial euclídeo $E$, llamaremos norma inducida por el producto escalar a la aplicación:

\begin{align}
\Vert \Vert :& E & \to & \mathbb{R}\\
             & \mathbf{u} & \mapsto & \sqrt{\mathbf{u}\cdot \mathbf{u}}
\end{align}
::: 

:::{prf:definition} Ortogonalidad
Diremos que dos vectores $\mathbf{u},\mathbf{v}\in E$ de un [espacio euclídeo](#espacio_euclideo) $E$ son ortogonales si se cumple que $\mathbf{u}\cdot\mathbf{v}=0$.

En ese caso lo denotaremos como $\mathbf{u}\perp\mathbf{v}$.
:::

:::{prf:definition} Sistema ortogonal
:label: sist_ortogonal
Diremos que un conjunto de vectores $S=\left\{\mathbf{u}_1,\mathbf{u}_2,\dots,\mathbf{u}_n\right\}$ es ortogonal si $\mathbf{u}_i\perp\mathbf{u}_j$ para todo $i=1,2,\dots, n$, $j=1,2,\dots, n$ con $i\neq j$.
:::

:::{prf:definition} Sistema ortonormal
:label: sist_ortonormal
Diremos que un conjunto de vectores $S=\left\{\mathbf{u}_1,\mathbf{u}_2,\dots,\mathbf{u}_n\right\}$ es ortonormal si es [ortogonal](#sist_ortogonal) y ademas $\Vert\mathbf{u}_i\Vert=1$ para todo $i=1,2,\dots, n$.
:::

:::{prf:definition} Base ortonormal
Diremos que un sistema de vectores es una base ortonormal de $U$ si es un sistema ortonormal y es una base de $U$.
:::

::::{prf:property}
La matriz asociada a un producto escalar en una base ortonormal (con respecto a dicho producto escalar) es la identidad.
:::{prf:proof}
:enumerated: false
:class: dropdown
Sabemos que $G=[g_{ij}]$ con $g_{ij} = \mathbf{e}_i\cdot\mathbf{e}_j$. Por ser el sistema ortogonal, cualquier elemento de fuera de la diagonal es cero, pues $i\neq j$ en ellos, y por ser ortonormal, cualquier elemento de la diagonal es $1$.
:::
::::

::::{prf:property}
Las matrices de cambio de base entre sistemas ortonormales son matrices ortogonales
:::{prf:proof}
:enumerated: false
:class: dropdown
Sean $\mathcal{B}$ y $\mathcal{B}'$ dos bases ortonormales de $E$. Por ser bases ortonormales, se tiene que $G=G'=I$. Por otra parte, por ser el producto escalar una forma bilineal, las matrices $G$ y $G'$ son congruentes:

$$
G'=P^\intercal G P
$$ 

Sustituyendo finalmente los valores de $G$ y $G'$ se obtiene que:
$$
I=P^\intercal P
S$
:::
::::


:::{prf:definition} Subespacios ortogonales
:label: subs_ortogonales
Dado un espacio vectorial euclídeo $E$, diremos que dos subespacios $U$ y $V$ son ortogonales, si se cumple que para cualquier $\mathbf{u}\in U$ y cualquier vector $\mathbf{v}\in V$, se tiene que $\mathbf{u}\perp\mathbf{v}$, es decir, si cualquier vector de $U$ es ortogonal a cualquier vector de $V$. En ese caso se denota como $U\perp V$.
:::

### Coeficientes de Fourier

:::{prf:definition} Coeficientes de Fourier
Dada una base ortogonal $\mathcal{B}={\mathbf{e}_1,\mathbf{e}_2,\dots,\mathbf{e}_n}$, llamamos coeficientes de Fourier del vector $\mathbf{v}$ con respecto a esa base a las cantidades:

$$
x_i = \frac{\mathbf{v}\cdot\mathbf{e}_i}{\|\mathbf{e}_i\|^2},\quad i=1,2,\dots n
$$

:::


## Proyección ortogonal

:::{prf:definition} Distancia inducida por una norma
Dado un espacio vectorial $E$ en el que tengamos definida una norma $\|\|$, llamamos distancia inducida por la norma a la función:
\begin{align}
d: & E\times E & \to & \mathbb{R}\\
   & (\mathbf{x},\mathbf{y}) & \mapsto & \Vert\mathbf{y}-\mathbf{x}\Vert
\end{align}
:::


## Ortogonalización de Gram-Schmidt
Dada una base $\mathcal{B}=\{\mathbf{u}_1, \mathbf{u}_2,\dots,\mathbf{u}_n\}$, no necesariamente ortogonal, el proceso de ortogonalización de Gram-Schmidt construye una base $\mathcal{B}'=\{\mathbf{v}_1, \mathbf{v}_2,\dots,\mathbf{v}_n\}$ que satisfaciendo:

- $\mathcal{B}'$ es ortogonal
- Para todo $k=1,2,\dots,n$, $\mathcal{L}(\{\mathbf{u}_1,\mathbf{u}_2,\dots, \mathbf{u}_k\})=\mathcal{L}(\{\mathbf{v}_1,\mathbf{v}_2,\dots, \mathbf{v}_k\})$
- Si $\mathcal{B}$ es ortogonal, entonces $\mathcal{B'}=\mathcal{B}$.


Para empezar, si queremos que $\mathcal{L}(\{\mathbf{v}_1\}) = \mathcal{L}(\{\mathbf{u}_1\})$ tiene que ser $\mathbf{v}_1=\alpha \mathbf{u}_1$ y si queremos que en el caso de que $\mathcal{B}$ sea ortogonal se cumpla que $\mathcal{B}'=\mathcal{B}$ solo nos deja la opción $\mathbf{v}_1=\mathbf{u}_1$.


- $\mathbf{v}_1 = \mathbf{u}_1$
- $\mathbf{v}_i = \mathbf{u}_i - \sum_{k=1}^{i-1}\mathrm{proy}_{\mathbf{v}_k}(\mathbf{u}_i)$ para $i=2,3,\dots,n$

::::{tab-set}
:::{tab-item} Python
:sync: tab_Python
```{code}python
:linenos:
:emphasize-lines: 10-15
import numpy as np
from numpy.typing import NDArray

real_array = NDArray[np.float64]

def proy(u: real_array, v: real_array) -> real_array:
    '''proy(u,v) devuelve la proyección de u sobre v'''
    return np.dot(u, v) / np.dot(v, v) * v

def Gramm_Schmidt(B: list[real_array]) -> list[real_array]:
    '''Calcula una base ortogonal mediante el proceso de Gramm-Schmidt'''
    B_ort: list[real_array] = []
    for u in B:
        B_ort.append(u - sum([proy(u, v) for v in B_ort]))
    return B_ort
```
:::
::::


## Diagonalización de formas cuadráticas

::::{prf:property} 
Los [subespacios propios](#subs_propio) de una matriz simétrica son [subespacios ortogonales](#subs_ortogonales) con respecto al producto escalar usual.
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

## Transformaciones ortogonales