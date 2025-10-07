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
\mathbf{0} = - \mathbf{u}_1 +  \beta_2\mathbf{u}_2 + \beta_3\mathbf{u}_3 + \dots + \beta_n\mathbf{u}_n 
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