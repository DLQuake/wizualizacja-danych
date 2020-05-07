import numpy as np

# możemy w łatwy sposób stworzyć macierz danego rozmiaru wypełnioną zerami lub jedynkami
zera = np.zeros((5,5))
jedynki = np.ones((4,4))
# warto sprawdzić jaki jest domyślny typ danych takich tablic
# można również stworzyć "pustą" macierz o podanych wymiarach, która wcale pusta nie jest
# wartości umieszczane są losowe
pusta = np.empty((2, 2))

# do elementów tablic możemy odwołać się tak jak do elementów np. listy czyli podając indeksy
poz_1 = pusta[1, 1]
poz_2 = pusta[0, 1]

# funkcja arange potrafi również tworzyć ciągi liczb zmiennoprzecinkowych
liczby = np.arange(1, 2, 0.1)
# podobnie działa funkcja linspace, której działanie jest równoważne tej samej funkcji w MATLAB-ie
liczby_lin = np.linspace(1, 2, 5)

# sprawdź również działanie funkcji logspace

# a teraz możemy utworzyć dwie macierze, najpierw wartości iterowane są w kolumnie a następnie w wierszu
z = np.indices((5, 3))
# wielowymiarowe macierze możemy również generować funkcją mgrid
x, y = np.mgrid[0:5, 0:5]

# podobnie jak w MATLAB-ie możemy tworzyć macierze diagonalne
mat_diag = np.diag([a for a in range(5)])
# w powyższym przykładzie stworzony wektor wartości zostanie umieszczony na głównej przekątnej macierzy
# możemy podać drugi parametr funkcji diag, który określa indeks przekątnej względem głównej przekątnej,
# która zostanie wypełniona wartościami podanego wektora
mat_diag_k = np.diag([a for a in range(5)], -2)

# Numpy jest w stanie stworzyć tablicę jednowymiarową z dodolnego obiektu iterowalnego (iterable)
z = np.fromiter(range(5), dtype='int32')
# ciekawą funkcją Numpy jest funkcja frombuffer, dzięki której możemy stworzyć np. tablicę znaków
marcin = b'Marcin'
mar = np.frombuffer(marcin, dtype='S1')
mar_2 = np.frombuffer(marcin, dtype='S2')
# powyższa funkcja ma jednak pewną wadę dla Pythona 3.x, która powoduje, że trzeba jawnie określać
# iż ciąg znaków przekazujemy jako ciąg bajtów co osiągamy poprzez podanie litery 'b' przed wartością
# zmiennej tekstowej. Można podobny efekt osiągnąć inaczej, sprawdź poniższe przykłady
marcin = 'Marcin'
mar_3 = np.array(list(marcin))
mar_3 = np.array(list(marcin), dtype='S1')
mar_3 = np.array(list(b'Marcin'))
mar_3 = np.fromiter(marcin, dtype='S1')
mar_3 = np.fromiter(marcin, dtype='U1')
# tablice numpy możemy w prosty sposób do siebie dodawać
mat = np.ones((2, 2))
mat2 = np.ones((2, 2))
mat = mat + mat2
print(mat)
# odejmować
print(mat - mat2)
# mnożyć
print(mat * mat)
# dzielić
print(mat / mat)