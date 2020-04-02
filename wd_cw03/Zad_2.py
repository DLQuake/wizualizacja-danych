#Wygeneruj losowo macierz 4x4 i wykorzystując Python Comprehension zdefiniuj listę, która będzie
#zawierała tylko elementy znajdujące się na przekątnej.

import random

macierz=[[random.randint(0, 9) for j in range (0, 4, 1)] for i in range (0, 4, 1)]
przekatna=[macierz[i][j] for i in range (0, 4, 1) for j in range (0, 4, 1) if i == j]
print("Macierz 4x4:")
print(macierz[0])
print(macierz[1])
print(macierz[2])
print(macierz[3])
print("Przekątna: ",przekatna)