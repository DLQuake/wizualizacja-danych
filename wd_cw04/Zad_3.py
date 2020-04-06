lista=["jabłko","jajko","mleko","chleb","woda","miód","szynka","kiełbasa","marchewka"]

with open("przykladowy_text_do_Zad_3.txt", "w") as plik:
    for text in lista:
        plik.write(str(text)+"\n")


with open("przykladowy_text_do_Zad_3.txt", "r") as plik:
    for text in plik:
        print(text, end="")