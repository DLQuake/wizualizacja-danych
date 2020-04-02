#Napisz skrypt, który pobiera od użytkownika trzy liczby a, b i c. Sprawdza następujące warunki:
def warunek():
    liczba1=input("Podaj pierwsza liczbe: ")
    liczba1=int(liczba1)

    liczba2=input("Podaj druga liczbe: ")
    liczba2=int(liczba2)

    liczba3=input("Podaj trzecia liczbe: ")
    liczba3=int(liczba3)


    if liczba1>0 and liczba1<=10:
        if liczba1>liczba2 or liczba2>liczba3:
            print("liczby",liczba1,liczba2,liczba3," Spelniaja wszytkie warunki")
        else:
            print("liczby",liczba1,liczba2,liczba3,"nie pelniaja wszytkich warunkow")
    else:
        print("liczby",liczba1,liczba2,liczba3,"nie pelniaja wszytkich warunkow")

warunek()
