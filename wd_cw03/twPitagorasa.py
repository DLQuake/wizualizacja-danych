def twierdzenie_pitagorasa(a,b):
    return (a**2+b**2)**0.5

a=float(input("Podaj pierwsza przyprostokatna: "))
b=float(input("Podaj druga przyprostokatna: "))

print("Dlugosc przeciwprostokatnej wynosi: ",twierdzenie_pitagorasa(a,b))

