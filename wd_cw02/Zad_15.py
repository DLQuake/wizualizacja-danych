#Napisz skrypt, w którym użytkownik ma podać liczbę i który będzie wyłapywał błąd gdy użytkownik
#poda literę zamiast cyfry.
try:
    liczba=int(input("Podaj liczbe: "))
    print("Podany znak jest liczba")
except:
    print("Podany znak nie jest liczba")
