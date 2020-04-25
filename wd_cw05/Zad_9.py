def wspak(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


lista=wspak(['S','T','A','T','E','K'])
print('lista wspak:', end=' ')
print(next(lista), end=', ')
print(next(lista), end=', ')
print(next(lista), end=', ')
print(next(lista), end=', ')
print(next(lista), end=', ')
print(next(lista))
print('-----------------------------------')
imie =wspak("Reks")
print('imie wspak:', end=' ')
print(next(imie), end=', ')
print(next(imie), end=', ')
print(next(imie), end=', ')
print(next(imie), end=', ')
print(next(imie))