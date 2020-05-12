#3.6. Iteracja tablic

import numpy as np
# generujemy macierz 3x2
b = np.arange(6).reshape(3,2)
print(b)
for a in b:
   # iterujemy wzdłuż pierwszej osi
   print(a)