import numpy as np

def macierz(n):
    mat = np.diag([2 for _ in range(n)])
    for indeks in range(1, n):
        vec = [2+(2*indeks) for _ in range(n-indeks)]
        mat += np.diag(vec, indeks)
        mat += np.diag(vec, -indeks)
    return mat

print(macierz(3))