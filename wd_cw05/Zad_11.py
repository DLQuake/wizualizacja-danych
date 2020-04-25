def ciąg_fibonacciego():
    a0=0
    a1=1
    while a0 > -1:
        a1+=a0
        a0=a1-a0
        yield a1-a0

wyraz=ciąg_fibonacciego()
for i in range(0, 11, 1):
    print('ciag('+str(i)+') =', next(wyraz))