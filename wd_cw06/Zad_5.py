import numpy as np

def wektor(n):
    return np.diag(range(n, 0, -1))

print(wektor(1))
print('\n------------------------\n')
print(wektor(2))
print('\n------------------------\n')
print(wektor(3))
print('\n------------------------\n')
print(wektor(4))
print('\n------------------------\n')
print(wektor(5))
print('\n------------------------\n')
print(wektor(5))