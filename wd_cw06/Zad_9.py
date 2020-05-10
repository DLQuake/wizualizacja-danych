import numpy as np

ciag_fibanaciego = np.empty((5, 5), dtype='int')
a = 0
b = 1
for i in range(0, 5, 1):
    for j in range(0, 5, 1):
        ciag_fibanaciego[i, j] = b
        b += a
        a = b-a

print(ciag_fibanaciego)