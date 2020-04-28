def miesiace():
    lista_miesiecy = ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec', 'Lipiec', 'Sierpień','Wrzesień', 'Październik', 'Listopad', 'Grudzień']
    for i in range(0, 12, 1):
        yield lista_miesiecy[i]

miesiac = miesiace()
for i in range(0, 12, 1):
    print(next(miesiac))