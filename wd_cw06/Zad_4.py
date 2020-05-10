import numpy as np

def potega(n,base):
    return np.logspace(1, n, num=n, base=base)


print(potega(1,0))
print(potega(2,1))
print(potega(3,2))
print(potega(4,3))
print(potega(5,4))