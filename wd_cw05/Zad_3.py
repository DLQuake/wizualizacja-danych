class Ksztalty:
    # definicja konstruktora
    def __init__(self, x, y):
        # deklarujemy atrybuty
        # self wskazuje że chodzi o zmienne właśnie definiowanej klasy
        self.x=x
        self.y=y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik

class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x =x
        self.y=x

    def __ge__(self, pom):
        if(self.x >= pom.x):
            return True
        else:
            return False

    def __gt__(self, pom):
        if(self.x > pom.x):
            return True
        else:
            return False

    def __le__(self, pom):
        if(self.x <= pom.x):
            return True
        else:
            return False

    def __lt__(self, pom):
        if(self.x < pom.x):
            return True
        else:
            return False

class KwadratowaLiteraL(Kwadrat):

    def obwod(self):
        return 8 * self.x

    def pole(self):
        return 3 * self.x * self.y

kwadrat1 = Kwadrat(5)
kwadrat2 = Kwadrat(5)
kwadrat3 = Kwadrat(10)

print('Pierwszy kwadrat: '+str(kwadrat1.x))
print('Drugi kwadrat: '+str(kwadrat2.x))
print('Trzeci kwadrat: '+str(kwadrat3.x))

print('--------------------------------------------------------------------')

print('__ge__:')
print('Czy kwadrat1 >= kwadrat2 ? Odpowwiedź: ',kwadrat1 >= kwadrat2)
print('Czy kwadrat1 <= kwadrat2 ? Odpowwiedź: ',kwadrat2 >= kwadrat1)
print('Czy kwadrat1 >= kwadrat3 ? Odpowwiedź: ',kwadrat1 >= kwadrat3)
print('Czy kwadrat1 <= kwadrat3 ? Odpowwiedź: ',kwadrat3 >= kwadrat1)
print('Czy kwadrat2 >= kwadrat3 ? Odpowwiedź: ',kwadrat2 >= kwadrat3)
print('Czy kwadrat2 <= kwadrat3 ? Odpowwiedź: ',kwadrat3 >= kwadrat2)

print('--------------------------------------------------------------------')

print('__gt__:')
print('Czy kwadrat1 > kwadrat2 ? Odpowwiedź: ',kwadrat1 > kwadrat2)
print('Czy kwadrat1 < kwadrat2 ? Odpowwiedź: ',kwadrat2 > kwadrat1)
print('Czy kwadrat1 > kwadrat3 ? Odpowwiedź: ',kwadrat1 > kwadrat3)
print('Czy kwadrat1 < kwadrat3 ? Odpowwiedź: ',kwadrat3 > kwadrat1)
print('Czy kwadrat2 > kwadrat3 ? Odpowwiedź: ',kwadrat2 > kwadrat3)
print('Czy kwadrat2 < kwadrat3 ? Odpowwiedź: ',kwadrat3 > kwadrat2)

print('--------------------------------------------------------------------')

print('__le__:')
print('Czy kwadrat1 <= kwadrat2 ? Odpowwiedź: ',kwadrat2 >= kwadrat1)
print('Czy kwadrat1 >= kwadrat2 ? Odpowwiedź: ',kwadrat1 >= kwadrat2)
print('Czy kwadrat1 <= kwadrat3 ? Odpowwiedź: ',kwadrat3 >= kwadrat1)
print('Czy kwadrat1 >= kwadrat3 ? Odpowwiedź: ',kwadrat1 >= kwadrat3)
print('Czy kwadrat2 <= kwadrat3 ? Odpowwiedź: ',kwadrat3 >= kwadrat2)
print('Czy kwadrat2 >= kwadrat3 ? Odpowwiedź: ',kwadrat2 >= kwadrat3)

print('--------------------------------------------------------------------')

print('__lt__:')
print('Czy kwadrat1 < kwadrat2 ? Odpowwiedź: ',kwadrat2 > kwadrat1)
print('Czy kwadrat1 > kwadrat2 ? Odpowwiedź: ',kwadrat1 > kwadrat2)
print('Czy kwadrat1 < kwadrat3 ? Odpowwiedź: ',kwadrat3 > kwadrat1)
print('Czy kwadrat1 > kwadrat3 ? Odpowwiedź: ',kwadrat1 > kwadrat3)
print('Czy kwadrat2 < kwadrat3 ? Odpowwiedź: ',kwadrat3 > kwadrat2)
print('Czy kwadrat2 > kwadrat3 ? Odpowwiedź: ',kwadrat2 > kwadrat3)