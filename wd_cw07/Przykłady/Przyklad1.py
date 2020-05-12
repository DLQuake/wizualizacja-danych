#1.1. Operacje arytmetyczne

import numpy as np
# inicjujemy dane
a = np.array( [20,30,40,50] )
b = np.arange( 4 )
print(b)
# wykonujemy operację i zapisujemy do nowej zmiennej
c = a-b
print(c)
# wykonujemy operację: kwadrat zawartości
print(b**2)
# możemy również zmodyfikować obecne zmienne
print(a)
a+=b
print(a)
a-=b
print(a)