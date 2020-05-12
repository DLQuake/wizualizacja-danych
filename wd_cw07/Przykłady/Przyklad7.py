#3.7 Iteracja tablic
import numpy as np
# generujemy macierz 3x2
b = np.arange(6).reshape(3,2)
print(b)
for a in b.flat:
   # iterujemy jakby to była macierz płaska
   print(a)