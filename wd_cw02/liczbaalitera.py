
liczba=int(input("Podaj liczbe: "))

try:
    print("znak ",liczba," jest liczba")
except InterruptedError:
    print("znak ",liczba," nie jest liczba")
