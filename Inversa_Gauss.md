# Calculo de la inversa mediante el método de Gauss
Supongamos que tenemos una matriz [regular](#matriz_regular) $A$ de tamaño $n$. Como sabemos, al ser regular, la matriz escalonada reducida correspondiente es $I_n$. Escribiendo las sucesivas operaciones necesarias para obtener la matriz escalonada como matrices tenemos que:

$$
P_kP_{k-1}\dots P_2P_1 A = I_n
$$

Por lo que llamando $P=P_kP_{k-1}\dots P_2P_1$ tenemos que $PA=I_n$ o lo que es lo mismo, $P$ es la inversa de $A$.

:::{prf:example}
Sea la matriz 
$$
A = \begin{bmatrix}
3 & 2 \\
4 & 4 
\end{bmatrix}
$$
cuyo determinante es $\det(A)=4$. Al tener determinante distinto de $0$ admite una inversa, y si la calculamos por el método de Kramer es:
$$
A^{-1}=\frac{1}{4}\begin{bmatrix}
4 & -2 \\
-4 & 3
\end{bmatrix}
=\begin{bmatrix}
1 & -\frac{1}{2} \\
-1 & \frac{3}{4}
\end{bmatrix}
$$

Vamos a obtener ahora su matriz escalonada reducida, paso a paso.  En primer lugar, podemos multiplicar la segunda fila por $3$. Escribiéndo la operación por medio de su matriz asociada sería:

$$
\begin{bmatrix}
3 & 2 \\
12 & 12 
\end{bmatrix}
=
\underset{P_1}{\underbrace{
\begin{bmatrix}
1 & 0 \\ 
0 & 3 
\end{bmatrix}}}
\underset{A}{\underbrace{\begin{bmatrix}
3 & 2 \\
4 & 4 
\end{bmatrix}}}
$$
Ahora podemos restar la primera fila multiplicada por $4$ a la segunda fila:

$$
\begin{bmatrix}
3 & 2 \\
0 & 4 
\end{bmatrix}
=
\underset{P_2}{\underbrace{\begin{bmatrix}
1 & 0 \\
-4 & 1
\end{bmatrix}
}}
\underset{P_1}{\underbrace{
\begin{bmatrix}
1 & 0 \\ 
0 & 3 
\end{bmatrix}}}
\underset{A}{\underbrace{\begin{bmatrix}
3 & 2 \\
4 & 4 
\end{bmatrix}}}
$$
Dividimos la segunda fila por $4$:

$$
\begin{bmatrix}
3 & 2 \\
0 & 1 
\end{bmatrix}
=
\underset{P_3}{\underbrace{\begin{bmatrix}
1 & 0 \\
0 & \frac{1}{4}
\end{bmatrix}
}}
\underset{P_2}{\underbrace{\begin{bmatrix}
1 & 0 \\
-4 & 1
\end{bmatrix}
}}
\underset{P_1}{\underbrace{
\begin{bmatrix}
1 & 0 \\ 
0 & 3 
\end{bmatrix}}}
\underset{A}{\underbrace{\begin{bmatrix}
3 & 2 \\
4 & 4 
\end{bmatrix}}}
$$

Le restamos a la primera fila la segunda multiplicada por $2$:

$$
\begin{bmatrix}
3 & 0 \\
0 & 1 
\end{bmatrix}
=
\underset{P_4}{\underbrace{\begin{bmatrix}
1 & -2\\
0 & 1 
\end{bmatrix}}}
\underset{P_3}{\underbrace{\begin{bmatrix}
1 & 0 \\
0 & \frac{1}{4}
\end{bmatrix}
}}
\underset{P_2}{\underbrace{\begin{bmatrix}
1 & 0 \\
-4 & 1
\end{bmatrix}
}}
\underset{P_1}{\underbrace{
\begin{bmatrix}
1 & 0 \\ 
0 & 3 
\end{bmatrix}}}
\underset{A}{\underbrace{\begin{bmatrix}
3 & 2 \\
4 & 4 
\end{bmatrix}}}
$$
y, finalmente, dividimos la primera fila por $3$

$$
\begin{bmatrix}
1 & 0 \\
0 & 1 
\end{bmatrix}
=
\underset{P_5}{\underbrace{\begin{bmatrix}
\frac{1}{3} & 0 \\
0 & 1
\end{bmatrix}
}}
\underset{P_4}{\underbrace{\begin{bmatrix}
1 & -2\\
0 & 1 
\end{bmatrix}}}
\underset{P_3}{\underbrace{\begin{bmatrix}
1 & 0 \\
0 & \frac{1}{4}
\end{bmatrix}
}}
\underset{P_2}{\underbrace{\begin{bmatrix}
1 & 0 \\
-4 & 1
\end{bmatrix}
}}
\underset{P_1}{\underbrace{
\begin{bmatrix}
1 & 0 \\ 
0 & 3 
\end{bmatrix}}}
\underset{A}{\underbrace{\begin{bmatrix}
3 & 2 \\
4 & 4 
\end{bmatrix}}}
$$

Por lo tanto, si llamamos $P=P_5P_4P_3P_2P_1$, tenemos que $P=A^{-1}$, pues $PA=I_2$.
:::

El método de Gauss consiste entonces en ir obteniendo $P$ de manera ordenada, pues si para calcular $A^{-1}$ tuviesemos que multiplicar $k$ matrices de tamaño $n$ no estaríamos obteniendo un algoritmo muy práctico. Sin embargo sabemos que $PI_n = P$, es decir, que la forma más fácil de obtener $P$ es realizar las mismas operaciones que le realizamos a $A$ a la matriz identidad. Así, el algoritmo de Gauss empieza por concatenar la matriz identidad de tamaño $n$ a la matriz cuya inversa queramos calcular y consiste en obtener la forma escalonada reducida por filas de dicha matriz ampliada. Una vez finalizado el proceso tendremos la matriz identidad donde se encontraba la matriz original y $P=A^{-1}$ donde se encontraba la matriz identidad. 

:::{prf:example}
Vamos a realizar el mismo ejemplo anterior, pero siguiendo el algoritmo de Gauss. Empezamos por la matriz ampliada con la identidad:

$$
\begin{bmatrix}
3 & 2 & 1 & 0 \\
4 & 4 & 0 & 1
\end{bmatrix}
$$

Y a partir de ahora vamos a obtener su matriz escalonada reducida:

En la segunda fila colocamos $3$ veces la segunda fila menos $4$ veces la primera:

$$
\begin{bmatrix}
3 & 2 & 1 & 0 \\
0 & 4 & -4 & 3
\end{bmatrix}
$$

Dividimos la segunda fila por $4$

$$
\begin{bmatrix}
3 & 2 & 1 & 0 \\
0 & 1 & -1 & \frac{3}{4}
\end{bmatrix}
$$

Le restamos a la primera fila $2$ veces la segunda

$$
\begin{bmatrix}
3 & 0 & 3 & -\frac{3}{2} \\
0 & 1 & -1 & \frac{3}{4}
\end{bmatrix}
$$

Y finalmente dividimos la primera fila por $3$.

$$
\begin{bmatrix}
1 & 0 & 1 & -\frac{1}{2} \\
0 & 1 & -1 & \frac{3}{4}
\end{bmatrix}
$$

Por lo que la matriz inversa es (la formada por las últimas dos columnas):

$$
A^{-1}=\begin{bmatrix}
1 & -\frac{1}{2} \\
-1 & \frac{3}{4}
\end{bmatrix}
$$


:::

El proceso puede parecer más tedioso que mediante el método de Kramer, pero a poco que la matriz sea grande, el método de Gauss es mucho más eficiente, pues evita calcular determinantes.