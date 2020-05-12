#1.2. Operacje na osiach

import numpy as np
b = np.arange(12).reshape(3,4)
print(b)
# suma całej macierzy
print(b.sum())
# suma każdej z kolumn
print(b.sum(axis=0))
# minimum każdego rzędu
print(b.min(axis=1))
# skumulowana suma dla rzędu
print(b.cumsum(axis=1))