#Napisz skrypt, który pobiera od użytkownika dwie wartości i mnoży je przez siebie. Wynik wyświetla
#na ekranie (użyj instrukcji readline() i write()).
def mnozeniewarosci():
    import sys

    print("Podaj wartosci")
    s=sys.stdin.readline()
    s=int(s)
    d=sys.stdin.readline()
    d=int(d)

    print(s*d)
mnozeniewarosci()