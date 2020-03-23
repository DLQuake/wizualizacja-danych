def monotonicznoscfunkcji(a,b):
    if a<0:
        print("Funkcja y =",a,"* x +",b,"jest malejaca")
        return a
    elif a==0:
        print("Funkcja y =",a,"* x +",b,"jest stała")
        return a
    else:
        print("Funkcja y =",a,"* x +",b,"jest rosnaca")
        return a

print(monotonicznoscfunkcji(-1,2))
print(monotonicznoscfunkcji(0,5))
print(monotonicznoscfunkcji(2,4))