import numpy as np

macierz_1 = np.array([1, 2, 3])
macierz_2 = np.array([4, 5, 6])

# z a.dot(b)
print('Iloczyn macierzy: ',macierz_1,' * ',macierz_2,' = ',macierz_1.dot(macierz_2))
print('Iloczyn macierzy: ',macierz_2,' * ',macierz_1,' = ',macierz_2.dot(macierz_1))

# z np.dot(a,b)
print('Iloczyn macierzy: ',macierz_1,' * ',macierz_2,' = ',np.dot(macierz_1,macierz_2))
print('Iloczyn macierzy: ',macierz_2,' * ',macierz_1,' = ',np.dot(macierz_2,macierz_1))