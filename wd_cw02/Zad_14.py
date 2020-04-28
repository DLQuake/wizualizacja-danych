import math
liczba = float(input('podaj liczbę rzeczywistą nieujemną: '))
try:
    wynik = math.sqrt(liczba)
    print('Pierwiastek z '+str(liczba)+' wynosi '+str(wynik))
except ValueError:
    print('Nie można obliczyć pierwiastka kwadratowego z liczby rzeczywistej ujemnej!')
