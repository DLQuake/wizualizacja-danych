#Napisz pętlę, która wyświetla liczby podzielne przez 5
def podzielneprzez5():
    for x in range(1,20,1):
        if x%5==0:
            print(str(x) + " ")

podzielneprzez5()