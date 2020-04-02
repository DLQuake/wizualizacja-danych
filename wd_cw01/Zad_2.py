#Stwórz skrypt kalkulator, w którym wykorzystać wszystkie podstawowe działania arytmetyczne
def kalkulator():

    print("MENU")
    print("1. Dodawanie (+)")
    print("2. Odejmowanie (-)")
    print("3. Mnozenie (*)")
    print("4. Dzielenie (/)")
    print("\n")
    znak=input("Wybierz działanie: ")
    if znak=="+":
        liczba1=int(input("Podaj pierwsza liczbe: "))
        liczba2=int(input("Podaj druga liczbe: "))

        suma = liczba1 + liczba2
        print(suma)
    elif znak=="-":
        liczba1=int(input("Podaj pierwsza liczbe: "))
        liczba2=int(input("Podaj druga liczbe: "))

        roznica=liczba1-liczba2
        print(roznica)
    elif znak=="*":
        liczba1=int(input("Podaj pierwsza liczbe: "))
        liczba2=int(input("Podaj druga liczbe: "))

        iloczyn=liczba1*liczba2
        print(iloczyn)
    elif znak=="/":
        liczba1=int(input("Podaj pierwsza liczbe: "))
        liczba2=int(input("Podaj druga liczbe: "))

        if liczba2!=0:
            dzielenie=liczba1/liczba2
            print(dzielenie)
        else:
            print("Nie mozna dzielic przez zero")
    else:
        print("Nie ma takiej opcji")

kalkulator()