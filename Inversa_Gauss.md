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


### Implementación del algoritmo de Gauss en un lenguaje de programación

A continuación se añade el código para el cálculo de una inversa por el método de Gauss escrito en diferentes lenguajes de programación. Se incluye una opción en [Fortran](https://fortran-lang.org/) por ser un lenguaje bastante parecido al lenguaje matemático y que, aunque actualmente está en desuso, todavía está presente en muchas librerías de cálculo numérico. Además se incluye una implementación en [Python](https://www.python.org/) así como opciones ya implementadas en paquetes numéricos como [Numpy](https://www.numpy.org) o simbólicos como [Sympy](https://www.sympy.org).
::::{tab-set}
:::{tab-item} Fortran
:sync: tab_fortran
```fortran
program test_inversa
        real :: A(2,2), A_inv(2,2)
        
        A(1,:) = [3., 2.]
        A(2,:) = [4., 4.]

        A_inv = Inversa(A)

        print*, "A:"
        do i = 1, 2
                print'(2F6.2)', A(i,:)
        end do
        print*, "A_inv:"
        do i = 1, 2
                print'(2F6.2)', A_inv(i,:)
        end do

        contains
        
                function Inversa(A) result(A_inv)
                        real, intent(in) :: A(:,:)
                        real :: A_inv(size(A, 1), size(A, 1))

                        integer :: i, j, n
                        real:: B(size(A,1), 2*size(A, 1))
                        
                        n = size(A, 1) ! numero de filas/columnas
                        
                        ! creamops la matriz ampliada
                        B(1:n, 1:n) = A   ! a la izquierda la matriz A
                        
                        B(1:n, n+1:2*n) = 0  ! a la derecha la matriz identidad
                        do i=1, n
                                B(i,n+i) = 1
                        end do

                        ! escalonamiento
                        do j=1, n 
                                B(j, :) = B(j, :)/B(j, j) !hacemos el pivote = 1
                                do i = j+1, n
                                        B(i,:) = B(i,:) - B(i,j)*B(j, :)
                                end do
                               
                        end do
                        ! reducción
                        do j=n, 1, -1
                                do i=j-1, 1, -1
                                        B(i,:) = B(i,:) - B(i,j)*B(j,:)
                                end do
                        end do
                        
                        ! obtenemos la inversa como la matriz a la derecha
                        A_inv = B(1:n, n+1: 2*n)

                end function

end program 
```
:::

:::{tab-item} Python
:sync: tab_python
```python
import numpy as np
from numpy.typing import NDArray

real_array = NDArray[np.float64]


def Inversa(A: real_array) -> real_array:
    # obtenemos el tamaño de la matriz A
    n = A.shape[0]
    # Concatenamos la matriz identidad de tamaño n a su derecha
    B = np.concatenate([A, np.eye(n)], axis=1)

    # Escalonamiento
    for j in range(n-1):  # para cada columna (excepto la última)
        B[j, :] = B[j, :] / B[j, j]  # hacemos el pivote = 1
        for i in range(j+1, n):  # para fila por debajo del pivote
            B[i, :] = B[i, :] - B[j, :]*B[i, j]
    B[n-1, :] = B[n-1, :] / B[n-1, n-1]  # hacemos el pivote = 1

    # Reducción
    for j in reversed(range(1, n)):
        for i in reversed(range(j)):
            B[i, :] = B[i, :] - B[j, :]*B[i, j]
    A_inv = B[:, n:]
    return A_inv

if __name__ == "__main__":
    A = np.array([[3, 2],
                  [4, 4]])
    A_inv = Inversa(A)
    print('A:')
    print(A)
    print('A_inv:')
    print(A_inv)
```
:::

:::{tab-item} Python+Numpy (numérico)
:sync: tab_numpy
```python
import numpy as np
from numpy.linalg import inv
A = np.array([[3, 2],
              [4, 4]])
print(A)
print(inv(A))
```
:::



:::{tab-item} Python + Sympy (simbólico)
:sync: tab_sympy
```python
from sympy import Matrix, pretty_print
A = Matrix([[3, 2],
            [4, 4]])
print("A:")
pretty_print(A)
print("A_inv:")
pretty_print(A.inv())
```
:::
::::

A continuación se muestran los resultados obtenidos:
::::{tab-set}
:::{tab-item} Fortran
:sync: tab_fortran
```shell
 A:
  3.00  2.00
  4.00  4.00
 A_inv:
  1.00 -0.50
 -1.00  0.75
```
:::
:::{tab-item} Python
:sync: tab_python
```shell
A:
[[3 2]
 [4 4]]
A_inv:
[[ 1.   -0.5 ]
 [-1.    0.75]]
```
:::
:::{tab-item} Python+Numpy
:sync: tab_numpy
```shell
A:
[[3 2]
 [4 4]]
A_inv:
[[ 1.   -0.5 ]
 [-1.    0.75]]
```
:::
:::{tab-item} Python+Sympy
:sync: tab_sympy
```shell
A:
⎡3  2⎤
⎢    ⎥
⎣4  4⎦
A_inv:
⎡1   -1/2⎤
⎢        ⎥
⎣-1  3/4 ⎦
```
:::

::::