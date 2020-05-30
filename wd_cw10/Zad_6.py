import pandas as pd
import matplotlib.pyplot as plt


etykiety = ['K', 'M']
wartosci = [100, 50]

plt.bar(etykiety, wartosci)
plt.subplot(3, 2, 1)
plt.xticks(rotation=45)
plt.ylabel('Ilość')
plt.xlabel('Płeć')
plt.show()

plt.plot(etykiety, wartosci)
plt.subplot(3, 2, 4)
plt.ylabel('Liczba')
plt.xlabel('Plec')
plt.legend()
plt.show()

plt.bar(etykiety, wartosci)
plt.subplot(325)
plt.ylabel('Liczba')
plt.xlabel('Plec')
plt.show()