#Napisz skrypt, w którym użytkownik ma podać liczbę i który będzie wyłapywał błąd gdy użytkownik
#poda literę zamiast cyfry.
liczba=int(input("Podaj liczbe: "))

try:
    print("znak ",liczba," jest liczba")
except InterruptedError:
    print("znak ",liczba," nie jest liczba")
