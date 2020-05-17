#Napisz skrypt, który pobiera od użytkownika zdanie i liczy w nim spacje. Wynik wyświetla na ekranie
#(użyj instrukcji input)
import sys

def liczbaspacji():
    a=input("Podaj tekst: ")
    print('\nW napisie spacja pojawia się',a.count(' '),'razy')


liczbaspacji()