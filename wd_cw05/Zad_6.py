class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


lista=Wspak(['S','T','A','T','E','K'])
print('lista wspak:', end=' ')
print(next(lista), end=', ')
print(next(lista), end=', ')
print(next(lista), end=', ')
print(next(lista), end=', ')
print(next(lista), end=', ')
print(next(lista))
print('-----------------------------------')
imie =Wspak("Reks")
print('imie wspak:', end=' ')
print(next(imie), end=', ')
print(next(imie), end=', ')
print(next(imie), end=', ')
print(next(imie), end=', ')
print(next(imie))