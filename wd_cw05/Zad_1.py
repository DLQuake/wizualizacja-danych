class Material:
    def __init__(self,rodzaj,dlugosc,szerokosc):
        self.rodzaj=rodzaj
        self.dlugosc=dlugosc
        self.szerokosc=szerokosc

    def wyświetl_nazwę(self):
        print("Rodaj materiału: "+str(self.rodzaj))
        print("Długość materiału: "+str(self.dlugosc))
        print("Szerokość materiału: "+str(self.szerokosc))

class Ubrania(Material):
    def __init__(self,rozmiar,kolor,dla_kogo):
        self.rozmiar=rozmiar
        self.kolor=kolor
        self.dla_kogo=dla_kogo

    def wyświetl_dane(self):
        print("Rozmiar ubrania: "+str(self.rozmiar))
        print("Kolor ubrania: "+str(self.kolor))
        print("Dla kogo jest to ubranie: "+str(self.dla_kogo))

class Sweter(Ubrania):
    def __init__(self,rodzaj_swetra):
        self.rodzaj_swetra=rodzaj_swetra

    def wyświetl_dane(self):
        print("Rodzaj swetra : "+str(self.rodzaj_swetra))

bawelna = Material('bawełna', 1, 1)
jedwab = Material('jedwab', 0.5, 0.5)
welna = Material('wełna', 5, 5)

bawelna.wyświetl_nazwę()
print("\n")
jedwab.wyświetl_nazwę()
print("\n")
welna.wyświetl_nazwę()
print("\n")
ubranie = Ubrania('XL', 'czarny', 'Jan Kowalski')
ubranie.wyświetl_dane()

print("\n")
sweter = Sweter('Rozpinany')
sweter.wyświetl_dane()