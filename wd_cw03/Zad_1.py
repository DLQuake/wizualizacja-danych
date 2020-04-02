#Zdefiniuj następujące zbiory, wykorzystując Python comprehension:
#A={1/x: x E <1,10>}
#B={1, 2, 4, 8,…, 2^10}
#C={x: xEB i x jest liczbą podzielną przez 4}

A = [1/x for x in range(11) if x!=0]
B = [2**i for i in range(10)]
C = [x for x in B if x%4==0]

print("A = ",A)
print("B = ",B)
print("C = ",C)