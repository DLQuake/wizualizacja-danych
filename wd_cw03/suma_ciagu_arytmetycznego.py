def suma_ciagu_arytmetycznego(a1,r,ile):
    return ile*(2*a1+(ile-1)*r)/2

print("Ciag arytmetyczny")

a1=float(input("Podaj pierwszy wyraz ciagu: "))
r=float(input("Podaj r: "))
ile=float(input("Podaj ilosc elementow ciagu: "))

print("Suma ciagu arytmetycznego wynosi ",suma_ciagu_arytmetycznego(a1,r,ile))