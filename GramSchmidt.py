import numpy as np
from numpy.typing import NDArray

real_array = NDArray[np.float64]


def proy(u: real_array, v: real_array) -> real_array:
    '''proy(u,v) devuelve la proyección de u sobre v'''
    return np.dot(u, v) / np.dot(v, v) * v


def Gram_Schmidt(B : list[real_array]) -> list[real_array]:
    B_ort: list[real_array] = []
    for u in B:
        B_ort.append(u - sum([proy(u, v) for v in B_ort]))
    return B_ort

if __name__=="__main__":
    B = [ np.array([1, 1, 0]), np.array([0, 1, 1])]
    B_ort = Gram_Schmidt(B)
    for v in B_ort:
        print(v)