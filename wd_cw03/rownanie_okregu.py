def rownanie_okregu(a = 0, b = 0, x = 0, y = 0):
    return ((x-a)**2+(y-b)**2)**0.5


print("Podaj Współrzędne środka okręgu to (a,b)")
a=input("a = ")
b=input("b = ")

print('Podaj punkt o współrzędnych (x,y)')
x=input("x = ")
y=input("y = ")

print("Promień okręgu ma długość równą: ",rownanie_okregu(float(a), float(b), float(x), float(y)))