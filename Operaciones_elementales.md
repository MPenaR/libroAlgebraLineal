# Operaciones elementales
Al final todo esto viene de los sistemas de ecuaciones. 


## Operaciones elementales por filas
Vamos a llamar operación elemental por filas a una de las $3$ transformaciones siguientes: 
- Intercambio de dos filas
- Multiplicación de una fila por un escalar distinto de $0$. 
- Suma de una fila a otra fila

Como vimos en BLA, la multiplicación matricial se puede entender como combinaciones de filas, por lo que a cada una de las anteriores operaciones le corresponde una matriz, $P$, de manera que $PA=B$ nos genera la matriz $B$ que se obtiene al realizar dichas operaciones elementales en $A$. Sabiendo esto, la manera más rápida de recordar la matriz asociada a cada operación elemental es realizar esa operación a la matriz identidad, pues $PI=P$, por lo que la matriz resultante de aplicar esa operación es la propia matriz asociada. Así tendremos que:

- La matriz que intercambia la segunda y la tercera fila (de una matriz con $4$ filas) sería:

$$
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

- La matriz que multiplica la segunda fila por $alpha$ en una matriz con $2$ filas será:

$$
\begin{bmatrix}
1 & 0 \\
0 & \alpha
\end{bmatrix}
$$

- Y la matriz que suma las filas $1$ y $3$ y las coloca en la primera fila de una matriz con $3$ filas será:

$$
\begin{vmatrix}
1 & 0 & 1 \\
0 & 1 & 0 \\
0 & 0 & 1 \\
\end{vmatrix}
$$

Es sencillo comprobar que las del primer tipo tienen determinante $-1$, las del segundo tienen determinante $\alpha\neq 0$ y las del tercero tienen determinante $1$, y por lo tanto, ninguna de ellas tiene determinante $0$. 


## Determinante del producto

::::{prf:property}
Dadas dos matrices $A,B\in\mathcal{M}_n$, se tiene que $\det(AB)=\det(A)\det(B)$.
::::


