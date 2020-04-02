#Napisz skrypt, który liczy pierwiastek z liczby podanej przez użytkownika jeśli użytkownik poda
#wartość ujemną to powinien być wyłapany błąd

import math
print("Liczenie piewiastkow")

liczba=input("Podaj liczbe: ")

if int(liczba)>0:
    print("Pierwiastek z ",liczba," wynosi ",math.sqrt(int(liczba)))
else:
    print("podales ujemna liczbe a nie mozna liczyc pierwiastkow z ujemnej liczby")
