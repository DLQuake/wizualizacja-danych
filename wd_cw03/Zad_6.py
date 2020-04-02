#Zdefiniuj funkcję, która na podstawie równania okręgu w postaci kanonicznej zwróci długość
#promienia. Funkcja ma przyjmować argumenty domyślne:
#Równanie okręgu dane jest wzorem:
#(x-a)^2+(y-b)^2=r^2
#gdzie (a,b) to środek okręgu a r to promień okręgu.
def rownanie_okregu(a = 0, b = 0, x = 0, y = 0):
    return ((x-a)**2+(y-b)**2)**0.5


print("Podaj Współrzędne środka okręgu to (a,b)")
a=input("a = ")
b=input("b = ")

print('Podaj punkt o współrzędnych (x,y)')
x=input("x = ")
y=input("y = ")

print("Promień okręgu ma długość równą: ",rownanie_okregu(float(a), float(b), float(x), float(y)))