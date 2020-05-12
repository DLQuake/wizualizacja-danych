#1.3. Mnożenie macierzy

import numpy as np
# inicjujemy dane
a = np.arange(3)
b = np.arange(3)
print(a.dot(b))  # iloczyn macierzy
print(np.dot(a,b)) # inny sposób