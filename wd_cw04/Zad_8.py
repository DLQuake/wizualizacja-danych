class Robaczek:
    def __init__(self,x,y,krok):
        self.x=x
        self.y=y
        self.krok=krok
    def __del__(self):
        print("Robaczek zjadł jabłko")
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

print("ZACZYNAMY GRĘ!\n")
print("GOTOWI!\n")
print("RUSZAMY!\n")
robaczek=Robaczek(0,0,1)
robaczek.pokaz_gdzie_jestes()
robaczek.idz_w_gore(500)
robaczek.pokaz_gdzie_jestes()
robaczek.idz_w_dol(100)
robaczek.pokaz_gdzie_jestes()
robaczek.idz_w_lewo(4000)
robaczek.pokaz_gdzie_jestes()
robaczek.idz_w_prawo(920)
robaczek.pokaz_gdzie_jestes()