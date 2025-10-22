# Coordenadas y cambios de coordenadas. 

Sea un espacio vectorial $V$ de dimension $n$. 

:::{prf:definition} Coordenadas de un vector. 
Llamaremos coordenadas de un vector $\mathbf{v}\in V$ en una base $\mathcal{B}=\{\mathbf{e}_1,\mathbf{e}_2,\dots\mathbf{e}_n\}$ de $V$ a los $n$ escalares $(x_1,x_2,\dots,x_n)\in\mathbb{K}^n$ que cumplen:
$$
\mathbf{v} = x_1\mathbf{e}_1 + x_2\mathbf{e}_2 +\dots + x_n\mathbf{e}_n
$$

Como ya demostramos, dichos escalares son únicos para cada vector $\mathbf{v}$ y base $\mathbf{B}$.
:::

Por comodidad denotaremos por  $(x_1,x_2,\dots,x_n)_\mathcal{B}$ a la [combinación lineal](#combinacion_lineal):
$$
(x_1,x_2,\dots,x_n)_\mathcal{B} = x_1\mathbf{e}_1+ x_2\mathbf{e}_2 \dots x_n \mathbf{e}_n
$$
de modo que, si $(x_1,x_2,\dots,x_n)$ son las coordenadas del vector $\mathbf{v}$ en la base $\mathcal{B}$, entonces $\mathbf{v}=(x_1,x_2,\dots,x_n)_\mathcal{B}$.

:::{prf:example} Polinomios en la base usual
Sea $\mathcal{B}=\{1,t,t^2\}$ la base usual del espacio vectorial $\mathbb{R}_2[t]$. Queremos calcular las coordenadas en dicha base de los polinomios $p_1(t)=1 - t^2$, $p_2(t)=t^2 - t$ y $p_3(t) = t^2 + t$.

Puesto que 
$$
p_1(t) = 1 + 0t + (-1)t^2
$$
entonces $p_1(t) = (1,0,-1)_\mathcal{B}$ y las coordenadas de $p_1$ en $\mathcal{B}$ serían la terna $(1,0,-1)$. Del mismo modo tenemos que 
$$
p_2(t) = (0,-1,1)_\mathcal{B},\quad p_3(t)=(0,1,1)_\mathcal{B}
$$
:::

## Isomorfismo de coordenadas

Como veremos un isomorfismo es una [aplicación lineal](#app_lineal) [biyectiva](#f_biyectiva). Dado un espacio vectorial $V$ de dimensión $n$ y una base $\mathcal{B}$, vamos a probar que la aplicación $T:V\to \mathbb{R}_n$ que a cada vector de $V$ le asigna sus coordenadas en la base $\mathcal{B}$, es una isomorfismo.

::::{prf:definition} Isomorfismo de coordenadas
Dado un espacio vectorial $V$ de dimensión $n$ y una base $\mathcal{B}$ de $V$, llamamos isomorfismo de coordenadas a la aplicación lineal:

$$
\begin{align}
T:V&\to&\mathbb{K}^n\\
\mathbf{v}=(x_1,x_2,\dots,x_n)_\mathcal{B}&\mapsto& (x_1,x_2,\dots,x_n)
\end{align}
$$

:::{prf:proof}
:enumerated: False
Vamos a probar en primer lugar que se trata de una aplicación lineal, y luego que es inyectiva y sobreyectiva.

Para probar que es lineal tenemos que probar que $T(\mathbf{u}+\mathbf{v})=T(\mathbf{u}) + T(\mathbf{v})$ y $T(\lambda\mathbf{u})=\lambda T(\mathbf{u})$, o dicho de otra manera, que las coordenadas de una combinación lineal de vectores son la combinación lineal de coordenadas. 

Sean $\mathbf{u} = (x_1, x_2,\dots, x_n)_\mathcal{B}$ y $\mathbf{v}=(y_1,y_2,\dots, y_n)_\mathcal{B}$ dos vectores cualesquiera de $V$. Por definición 

$$
\mathbf{u}+\mathbf{v} = x_1\mathbf{e}_1+x_2\mathbf{e}_2+\dots+x_n\mathbf{e}_n +y_1\mathbf{e}_1+y_2\mathbf{e}_2+\dots+ y_n\mathbf{e}_n
$$
y reordenando las sumas
$$
\mathbf{u}+\mathbf{v} = (x_1+y_1)\mathbf{e}_1+(x_2+y_2)\mathbf{e}_2+\dots+(x_n+y_n)\mathbf{e}_n
$$

por lo que $\mathbf{u}+\mathbf{v}=(x_1+y_1,x_2+y_2, \dots, x_n+y_n)_\mathcal{B}$. De manera análoga se demuestra que $\lambda \mathbf{v}=(\lambda x_1,\lambda x_2,\dots, \lambda x_n)_B$.

Demostrar que es [sobreyectiva](#f_sobreyectiva) es sencillo pues para cualquier elemento $(x_1,x_2,\dots,x_n)\in\mathbb{R}^n$ podemos construir el vector:

$$
\mathbf{v}=x_1\mathbf{e}_1+x_2\mathbf{e}_2+\dots+x_n\mathbf{e}_n
$$

tal que $T(\mathbf{v})=(x_1,x_2,\dots,x_n)$.

Para demostrar que es [inyectiva](#f_inyectiva) suponemos que tenemos dos vectores $\mathbf{u}$ y $\mathbf{v}$ tal que $\mathbf{u}\neq\mathbf{v}$. Si ambos vectores tuviesen las mismas coordenadas $(x_1,x_2,\dots, x_n)$ entonces tendríamos que:

$$
\mathbf{v}=(x_1,x_2,\dots,x_n)_\mathcal{B}=\mathbf{u}
$$

lo cual implicaría que $\mathbf{u}=\mathbf{v}$, en contra de lo que habíamos supuesto.

:::
::::




:::{prf:definition} Espacios isomorfos
Decimos que dos espacios vectoriales son isomorfos si existe un isomorfismo entre ellos.
:::

::::{prf:property}
Todo es espacio vectorial real de dimensión $n$ es isomorfo a $\mathbb{R}^n$. Del mismo modo, todo espacio vectorial complejo de dimensión $n$ es isomorfo a $\mathbb{C}^n$.
:::{prf:proof}
:enumerated: false
:class: dropdown
Como acabamos de ver, en ambos casos podemos definir el isomorfismo de coordenadas, entre $V$ y $\mathbb{R}^n$ o $\mathbb{C}^n$ respectivamente.
:::
::::