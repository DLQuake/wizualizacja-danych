import numpy as np
# generujemy macierz 3x2
b = np.arange(9).reshape(3,3)
print(b)
for a in b.flat:
   # iterujemy jakby to była macierz płaska
   print(a,end=' ')