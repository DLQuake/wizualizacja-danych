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

    def __add__(self,pom):
        return self.x + pom.x

class KwadratowaLiteraL(Kwadrat):

    def obwod(self):
        return 8 * self.x

    def pole(self):
        return 3 * self.x * self.y

figura = Kwadrat(5)
figura2 = Kwadrat(6)
figura3 = Kwadrat(figura + figura2)
print('Wymiary pierwszej figury:', figura.x,'x', figura.y)
print('Wymiary drugiej figury:', figura2.x,'x', figura2.y)
print('Wymiary trzeciej figury:', figura3.x,'x', figura3.y)
