def ilosc_produnktow(**lista_zakupow):
    suma = 0.0
    for i in lista_zakupow:
        suma+=float(lista_zakupow[i])
    return suma


print('liczba wszystkich produktów:', ilosc_produnktow(zupka_chinska=6,zeszyt_A4=5,jabłko=4, sok_owocowy=3, coca_cola_1_5L=1, banany=7))