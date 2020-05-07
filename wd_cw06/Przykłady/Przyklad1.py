import numpy as np

# inicjalizacja tablicy
a = np.array([0, 1])
# lub
a = np.arange(2)
print(a)
# wypisanie typu zmiennej tablicy (nie jej elementów) - ndarray
print(type(a))
# sprawdzenie typu danych tablicy
print(a.dtype)
# inicjalizacja tablicy z konkretnym typem danych
a = np.arange(2, dtype='int64')
print(a.dtype)
# zapisanie kopii tablicy jako tablicy z innym typem
b = a.astype('float')
print(b)
# wypisanie rozmiarów tablicy
print(b.shape)
# można też sprawdzić ilość wymiarów tablicy
print(a.ndim)

# stworzenie tablicy wielowymiarowej może wyglądać tak
# parametrem przekazywanym do funkcji array jest obiekt, który zostanie skonwertowany na tablicę
# może to być Pythonowa lista
m = np.array([np.arange(2), np.arange(2)])
print(m)
# ponownie typem jest ndarray
print(type(m))