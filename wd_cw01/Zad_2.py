#Stwórz skrypt kalkulator, w którym wykorzystać wszystkie podstawowe działania arytmetyczne
import sys,os,msvcrt
def kalkulator():

    while True:
        print("___________MENU PROGRAMU__________")
        print("1. Dodawanie")
        print("2. Odejmowanie")
        print("3. Mnozenie")
        print("4. Dzielenie zmiennoprzecinkowe")
        print("5. Dzielenie całkowite")
        print("6. Dzielenie z resztą")
        print("7. Potęgowanie")
        print("8. Koniec")
        print("\n")
        znak=input("Wybierz numer działania: ")
        if znak=="1":
            liczba1=int(input("Podaj pierwsza liczbe: "))
            liczba2=int(input("Podaj druga liczbe: "))

            suma = liczba1 + liczba2
            print('Wynik: ',suma)
        elif znak=="2":
            liczba1=int(input("Podaj pierwsza liczbe: "))
            liczba2=int(input("Podaj druga liczbe: "))

            roznica=liczba1-liczba2
            print('Wynik: ',roznica)
        elif znak=="3":
            liczba1=int(input("Podaj pierwsza liczbe: "))
            liczba2=int(input("Podaj druga liczbe: "))

            iloczyn=liczba1*liczba2
            print('Wynik: ',iloczyn)
        elif znak=="4":
            liczba1=int(input("Podaj pierwsza liczbe: "))
            liczba2=int(input("Podaj druga liczbe: "))

            if liczba2!=0:
                dzielenie=liczba1/liczba2
                print('Wynik: ',dzielenie)
            else:
                print("Nie mozna dzielic przez zero")
        elif znak=="5":
            liczba1=int(input("Podaj pierwsza liczbe: "))
            liczba2=int(input("Podaj druga liczbe: "))

            if liczba2!=0:
                dzielenie=liczba1//liczba2
                print('Wynik: ',dzielenie)
            else:
                print("Nie mozna dzielic przez zero")
        elif znak=="6":
            liczba1=int(input("Podaj pierwsza liczbe: "))
            liczba2=int(input("Podaj druga liczbe: "))

            if liczba2!=0:
                dzielenie=liczba1%liczba2
                print('Wynik: ',dzielenie)
            else:
                print("Nie mozna dzielic przez zero")
        elif znak=="7":
            liczba1=int(input("Podaj pierwsza liczbe: "))
            liczba2=int(input("Podaj druga liczbe: "))

            potega=liczba1**liczba2
            print('Wynik: ',potega)
        elif znak=='8':
            sys.exit(0)
        else:
            print("Nie ma takiej opcji")
        znak=sys.stdin.read(1)
        os.system('cls')

kalkulator()