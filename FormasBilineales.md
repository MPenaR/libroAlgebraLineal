# Formas bilineales

Definimos una forma bilineal como una aplicación


:::{prf:definition} Forma bilineal
:label: forma_bilineal
Dado un espacio vectorial $V$ sobre el cuerpo de escalares $\mathbb{K}$ decimos que:

\begin{align}
f:V\times V  & \to \mathbb{K} \\
(\mathbf{x},\mathbf{y}) & \mapsto f(\mathbf{x}, \mathbf{y})
\end{align}

es una forma bilineal si es [lineal](#app_lineal) en ambos argumentos:

- **Linealidad en el primer argumento:** Para todo $\alpha,\beta\in\mathbb{K}$ y todo $\mathbf{x},\mathbf{y},\mathbf{z}\in V$ se tiene que:

$$
f(\alpha \mathbf{x} + \beta \mathbf{y}, \mathbf{z}) = \alpha f(\mathbf{x}, \mathbf{z}) + \beta f( \mathbf{y}, \mathbf{z}) 
$$
- **Linealidad en el segundo argumento:** Para todo $\alpha,\beta\in\mathbb{K}$ y todo $\mathbf{x},\mathbf{y},\mathbf{z}\in V$ se tiene que:

$$
f(\mathbf{x},  \alpha \mathbf{y}+ \beta\mathbf{z}) = \alpha f(\mathbf{x}, \mathbf{y}) + \beta f( \mathbf{x}, \mathbf{z}) 
$$

:::


:::{prf:definition} Forma sesquilineal
:label: forma_sesquilineal
Dado un espacio vectorial $V$ sobre  $\mathbb{C}$ decimos que:

\begin{align}
f:V\times V  & \to \mathbb{C} \\
(\mathbf{x},\mathbf{y}) & \mapsto f(\mathbf{x}, \mathbf{y})
\end{align}

es una forma sesquilineal si es antilineal en el primer argumento y [lineal](#app_lineal) en el segundo:

- **Antilinealidad en el primer argumento:** Para todo $\alpha,\beta\in\mathbb{C}$ y todo $\mathbf{x},\mathbf{y},\mathbf{z}\in V$ se tiene que:

$$
f(\alpha \mathbf{x} + \beta \mathbf{y}, \mathbf{z}) = \overline{\alpha} f(\mathbf{x}, \mathbf{z}) + \overline{\beta} f( \mathbf{y}, \mathbf{z}) 
$$
- **Linealidad en el segundo argumento:** Para todo $\alpha,\beta\in\mathbb{C}$ y todo $\mathbf{x},\mathbf{y},\mathbf{z}\in V$ se tiene que:

$$
f(\mathbf{x},  \alpha \mathbf{y}+ \beta\mathbf{z}) = \alpha f(\mathbf{x}, \mathbf{y}) + \beta f( \mathbf{x}, \mathbf{z}) 
$$

donde $\overline{\alpha}$ denota al conjugado de $\alpha$.
:::



:::{prf:example} Producto escalar Euclídeo
En $\mathbb{R}^3$ podemos definir la forma bilineal dada por:
$$
f((x_1,x_2,x_3),(y_1,y_2,y_3))=(x_1,x_2,x_3)\cdot(y_1,y_2,y_3) = x_1y_1 + x_2y_2 + x_3y_3
$$
:::

:::{prf:example} Determiante de una matriz $2\times2$:
En $\mathbb{R}^2$ podemos definir la forma bilineal dada por:

$$
f((x_1,x_2), (y_1,y_2)) = \begin{vmatrix} x_1 & y_1 \\ x_2 & y_2 \end{vmatrix} = x_1y_2 - x_2y_1
$$
:::

## Matriz asociada a una forma bilineal en una base

Al igual que ocurría con las aplicaciones lineales, debido a la linealidad, conocer los valores de la forma bilineal en los elementos de una base nos va a permitir conocer sus valores en cualquier otro par de vectores, conocidas sus coordenadas en dicha base.

Supongamos que  tenemos una forma $f:V\times V \to \mathbb{K}$, y una base $\mathcal{B}=\left\{\mathbf{u}_1,\mathbf{u}_2,\dots,\mathbf{u}_n\right\}$ de $V$. Si queremos conocer el valor de $f(\mathbf{x}, \mathbf{y})$ en dos vectores cuales quiera $\mathbf{x}=\left(x_1,x_2,\dots,x_n\right)_\mathcal{B}$ e $\mathbf{y}=\left(y_1,y_2, \dots, y_n\right)_\mathcal{B}$. Entonces 

\begin{align}
f(\mathbf{x},\mathbf{y}) &=f\left(\sum_{i=1}^n x_i\mathbf{u}_i,\sum_{j=1}^n y_j\mathbf{u}_j\right)\\
                         &=\sum_{i=1}^n x_if\left(\mathbf{u}_i,\sum_{j=1}^n y_j\mathbf{u}_j\right)\quad\text{linealidad en el primer argumento}\\
                         &=\sum_{i=1}^n x_i\sum_{j=1}^n y_jf\left(\mathbf{u}_i,\mathbf{u}_j\right)\quad\text{linealidad en el segundo argumento}\\
                         &=\sum_{i=1}^n \sum_{j=1}^n x_i f\left(\mathbf{u}_i,\mathbf{u}_j\right) y_j
\end{align}

Por lo que definiendo la matriz $A=[a_{ij}]$ con $a_{ij}=f\left(\mathbf{u}_i,\mathbf{u}_j\right)$, tenemos que:

$$
f(\mathbf{x},\mathbf{y})=\sum_{i=1}^n \sum_{j=1}^n x_i a_{ij} y_j=X^\intercal A Y
$$

es decir

$$
f(\mathbf{x},\mathbf{y}) = \begin{bmatrix}x_1 & x_2 & \dots & x_n\end{bmatrix}\begin{bmatrix}f(\mathbf{u}_1,\mathbf{u}_1) & f(\mathbf{u}_1,\mathbf{u}_2) & \dots & f(\mathbf{u}_1,\mathbf{u}_n) \\
f(\mathbf{u}_2,\mathbf{u}_1) & f(\mathbf{u}_2,\mathbf{u}_2) & \dots & f(\mathbf{u}_2,\mathbf{u}_n) \\
\vdots & \ddots & \ddots & \vdots \\
f(\mathbf{u}_n,\mathbf{u}_1) & f(\mathbf{u}_n,\mathbf{u}_2) & \dots & f(\mathbf{u}_n,\mathbf{u}_n)\end{bmatrix}\begin{bmatrix}y_1 \\ y_2 \\ \vdots \\ y_n\end{bmatrix}
$$

### Cambio de base de la matriz asociada a una forma bilineal

Buscamos una matriz $A'$ que cumpla que, para cualquier par de vectores $X$ e $Y$:

$$
X^\intercal A Y = f(\mathbf{x},\mathbf{y}) = X'^\intercal A'Y'
$$

donde, llamando $P$ a la matriz de cambio de base de $\mathcal{B}'$ a $\mathcal{B}$, se tiene que $X=PX'$ e $Y=PY'$. Por lo tanto, sustituyendo en la igualdad anterior tenemos que

$$
(PX')^\intercal A PY'  = X'^\intercal A'Y'
$$
o lo que es lo mismo
$$
X'^\intercal P^\intercal A PY'  = X'^\intercal A'Y',\quad\forall X', Y'
$$
de donde se deduce que $A'=P^\intercal A P$. 

Cuando dos matrices están asociadas a la misma forma bilineal en bases diferentes decimos que son matrices congruentes. 

:::{prf:definition} Matrices congruentes
Dadas dos matrices $A$ y $B$ decimos que son congruentes si existe una tercera matriz $P$, regular, tal que:

$$
B = P^{\intercal} A P 
$$
:::




:::{prf:definition} Forma bilineal simétrica
:label: forma_simetrica
Decimos que una forma bilineal $f:V\times V \to \mathbb{K}$ es simétrica si para todo $\mathbf{x},\mathbf{y}\in V$ se cumple que $f(\mathbf{x},\mathbf{y})=f(\mathbf{y},\mathbf{x})$.
:::

Por ejemplo, la forma bilineal definida en el ejemplo BLA BLA es simétrica.

:::{prf:definition} Forma bilineal antisimétrica
Decimos que una forma bilineal $f:V\times V \to \mathbb{K}$ es antisimétrica si para todo $\mathbf{x},\mathbf{y}\in V$ se cumple que $f(\mathbf{x},\mathbf{y})=-f(\mathbf{y},\mathbf{x})$.
:::

En particular, toda forma bilineal antisimétrica cumple que $f(\mathbf{x},\mathbf{x})=0$ para todo $\mathbf{x}\in V$.


:::{prf:definition} Forma sesquilineal hermítica
:label: forma_hermitica
Decimos que una forma sesquilineal $f:V\times V \to \mathbb{C}$ es hermítica si para todo $\mathbf{x},\mathbf{y}\in V$ se cumple que:
$$
f(\mathbf{y},\mathbf{x}) = \overline{f(\mathbf{x},\mathbf{y})}
$$
:::

En particular, toda forma sesquilineal cumple que $\mathfrak{Im}(f(\mathbf{x},\mathbf{x}))=0$ para cualquier $\mathbf{x}\in V$.

::::{prf:property}
La matriz asociada a una forma hermítica es una matriz hermítica.
:::{prf:proof}
:enumerated: false
:class: dropdown
Se tiene que, para todo $\mathbf{x},\mathbf{y} \in V$:
\begin{align}
X^* A Y &= f(\mathbf{x},\mathbf{y}) \\
                &= \overline{f(\mathbf{y},\mathbf{x})} \\
                &= \overline{Y^* A X}\\
                &= Y^\intercal \overline{A} \overline{X} \\
                &= X^* A^* Y
\end{align}

por lo que $A=A^*$.
::: 
::::

:::{prf:definition} Forma definida positiva
:label: def_positiva
Dada una forma bilineal real, diremos que es definida positiva si cumple que, para todo $\mathbf{x}\neq \mathbf{0}$ se tiene que $f(\mathbf{x},\mathbf{x})>0$.
:::

:::{prf:definition} Forma definida negativa
:label: def_negativa
Dada una forma bilineal real, diremos que es definida negativa si cumple que, para todo $\mathbf{x}\neq \mathbf{0}$ se tiene que $f(\mathbf{x},\mathbf{x})<0$.
:::


### Diagonalización por congruencia

Decimos que una forma bilineal $f:V\times V \to \mathbb{K}$ es diagonalizable si existe una base $\mathcal{B}$ de $V$ en la que la matriz asociada a $f$ sea diagonal.

:::{prf:definition} Diagonalización por congruencia
Dada una matriz $A$ decimos que $A$ es diagonalizable por congruencia si existe una matriz regular $P$ y una matriz diagonal $D$ tal que:



$$
A = P D P^\intercal
$$
:::
