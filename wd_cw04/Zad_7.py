class Robaczek:
    def __init__(self,x,y,krok):
        self.x=x
        self.y=y
        self.krok=krok
    def idz_w_gore(self,ile_krokow):
        self.y+=ile_krokow*self.krok
    def idz_w_dol(self,ile_krokow):
        self.y-=ile_krokow*self.krok
    def idz_w_lewo(self,ile_krokow):
        self.x-=ile_krokow*self.krok
    def idz_w_prawo(self,ile_krokow):
        self.x+=ile_krokow*self.krok
    def pokaz_gdzie_jestes(self):
        print("Robaczek znajduje sie na pozycji ( "+str(self.x),", "+str(self.y),")")

print("Przykład kiedy krok jest rowny 1 czyli robaczek wykonuje jakieś kroki bo np wyczuł jakieś pyszności\n")
robaczek=Robaczek(0,0,1)
robaczek.pokaz_gdzie_jestes()
robaczek.idz_w_gore(50)
robaczek.pokaz_gdzie_jestes()
robaczek.idz_w_dol(10)
robaczek.pokaz_gdzie_jestes()
robaczek.idz_w_lewo(40)
robaczek.pokaz_gdzie_jestes()
robaczek.idz_w_prawo(90)
robaczek.pokaz_gdzie_jestes()

print("\n---------------------------------------\n")

print("Przykład kiedy krok jest rowny 0 czyli robaczek nie wykonuje żadnego kroku bo np nie ma jabłka dla niego\n")
robaczek=Robaczek(0,0,0)
robaczek.pokaz_gdzie_jestes()
robaczek.idz_w_gore(50)
robaczek.pokaz_gdzie_jestes()
robaczek.idz_w_dol(10)
robaczek.pokaz_gdzie_jestes()
robaczek.idz_w_lewo(40)
robaczek.pokaz_gdzie_jestes()
robaczek.idz_w_prawo(90)
robaczek.pokaz_gdzie_jestes()