import numpy as np
# cięcie (slicing) tablic numpy można wykonać za pomocą wartości z funkcji slice lub range
a = np.arange(10)
s = slice(2, 7, 2)
print(a[s])
s = range(2, 7, 2)
print(a[s])
# # możemy ciąć tablice również w sposób znany z cięcia list (efekt jak wyżej)
print(a[2:7:2])
# # lub tak
print(a[1:])
print(a[2:5])
# w podobny sposób postępujemy w przypadku tablic wielowymiarowych
mat = np.arange(25)
# teraz zmienimy kształt tablicy jednowymiarowej na macierz 5x5
mat = mat.reshape((5,5))
print(mat)
print(mat[1:])  # od drugiego wiersza
print(mat[:, 1])  # druga kolumna jako wektor
print(mat[..., 1])  # to samo z wykorzystaniem ellipsis (...)
print(mat[:, 1:2])  # druga kolumna jako ndarray
print(mat[:, -1:])  # ostatnia kolumna
print(mat[1:3, 2:4])  # 2 i 3 kolumna dla 3 i 5 wierszu
print(mat[:, range(2,6,2)])  # 3 i 5 kolumna
# bardziej zaawansowane, lecz trudniejsze do zrozumienia cięcie można osiąnąć wg. poniższego przykładu
# y będzie tablicą zawierającą wierzchołki macierzy x
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
rows = np.array([[0, 0], [3,3]])
cols = np.array([[0, 2], [0,2]])
y = x[rows, cols]