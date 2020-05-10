import numpy as np

malina = np.array(list('malina'))
lizak = np.array(list('lizak'))
jagoda = np.array(list('jagoda'))

wykreslanka = np.empty((6, 6), dtype='str')

wykreslanka[:, 0] = malina
wykreslanka[2,:5] = lizak
wykreslanka[1,::-1] = jagoda

print(wykreslanka)