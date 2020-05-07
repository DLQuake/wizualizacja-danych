import numpy as np

def tablica(n):
    return np.arange(1,n*n+1).reshape((n,n))

print(tablica(1))
print('\n------------------------\n')
print(tablica(2))
print('\n------------------------\n')
print(tablica(3))
print('\n------------------------\n')
print(tablica(4))
print('\n------------------------\n')
print(tablica(5))