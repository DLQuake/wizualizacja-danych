class Pracownik:
    __prywatna = "tajne hasło"

    def __init__(self, imie):
        self.imie = imie

janek = Pracownik("Janek")
print(janek.__prywatna)    # to nie zadziała
print(janek._Pracownik__prywatna)   # ale to już tak