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

    return B[:, n:]
if __name__=="__main__":
    from sympy import Matrix, pretty_print

    A = Matrix([[3, 2],
                [4, 4]])
    print("A:")
    pretty_print(A)
    print("A_inv:")
    pretty_print(A.inv())

    #nuestra solución:
    A = np.array([[3, 2],
                  [4, 4]])
    A_inv = Inversa(A)
    print('A:')
    print(A)
    print('A_inv:')
    print(A_inv)

    from numpy.linalg import inv
    A = np.array([[3, 2],
                  [4, 4]])
    A_inv = inv(A)
    print('A:')
    print(A)
    print('A_inv:')
    print(A_inv)
