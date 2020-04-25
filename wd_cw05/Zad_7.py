class Indeks_parzysty:

    def __init__(self, data):
        self.data = data
        self.indeks = -2

    def __iter__(self):
        return self

    def __next__(self):
        if self.indeks >= len(self.data):
            raise StopIteration
        self.indeks += 2
        return self.data[self.indeks]

liczby = Indeks_parzysty([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(next(liczby), end=', ')
print(next(liczby), end=', ')
print(next(liczby), end=', ')
print(next(liczby), end=', ')
print(next(liczby), end=', ')
print(next(liczby))