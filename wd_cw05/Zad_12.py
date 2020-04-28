def lista_miesiacy():
    lista_miesiecy = ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec', 'Lipiec', 'Sierpień','Wrzesień', 'Październik', 'Listopad', 'Grudzień']
    for i in range(0, 12, 1):
        yield lista_miesiecy[i]

miesiace = lista_miesiacy()
for i in range(0, 12, 1):
    print(next(miesiace))
