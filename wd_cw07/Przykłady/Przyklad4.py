#1.4. Operacje na tablicach różnej dokładności (upcasting)

import numpy as np
# macierz całkowita
a = np.ones(3, dtype=np.int32)
print(a.dtype.name)
# macierz zmiennoprzecinkowa
b = np.linspace(0,np.pi,3)
print(b.dtype.name)
# wynikiem jest macierz zmiennoprzecinkowa
c = a+b
print(c)
print(c.dtype.name)
# wynikiem jest macierz liczb zespolonych
d = np.exp(c*1j)
print(d)
print(d.dtype.name)