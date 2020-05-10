import numpy as np

def pionowo_czy_poziomo(tab,kierunek):
    if kierunek == 'poziomo':
        # nieparzysta liczba wierszy
        if tab.shape[0] % 2 != 0:
            print("Tablica posiada nieprzystą liczbę wierszy")
            return
        p1 = tab[0:int(tab.shape[0]/2), :]
        p2 = tab[int(tab.shape[0]/2):, :]
        print("***** część 1 *****")
        print(p1)
        print("***** część 2 *****")
        print(p2)
    elif kierunek == "pionowo":
        if tab.shape[1] % 2 != 0:
            print("Tablica posiada nieprzystą liczbę wierszy")
            return
        p1 = tab[:, 0:int(tab.shape[1]/2)]
        p2 = tab[:, int(tab.shape[0] / 2):]
        print("***** część 1 *****")
        print(p1)
        print("***** część 2 *****")
        print(p2)

pionowo_czy_poziomo(np.arange(36).reshape((6,6)),'poziomo')
print('\n------------------------\n')
pionowo_czy_poziomo(np.arange(25).reshape((5,5)),'pionowo')
print('\n------------------------\n')
pionowo_czy_poziomo(np.arange(25).reshape((5,5)),'poziomo')
print('\n------------------------\n')
pionowo_czy_poziomo(np.arange(36).reshape((6,6)),'pionowo')