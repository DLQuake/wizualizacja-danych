liczby=[]
for x in range(1,100,1):
        if x%4==0:
            liczby+=[x]

plik=open("liczby_podzielne_przez_4_dla_Zad_1_Zad_2.txt","w+")

plik.writelines(str(liczby))

plik.close()