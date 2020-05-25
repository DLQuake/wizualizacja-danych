import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel('datasets/imiona.xlsx')
print(df)

grupa = df.groupby(['Plec']).agg({'Liczba':['sum']})
print(grupa)
plt.subplot(1, 3, 1)
wykres = grupa.plot.bar()
wykres.set_ylabel('Liczba')
wykres.set_xlabel('Plec')
wykres.legend()
plt.title('liczba urodzonych chłopców i dziewczynek')
plt.show()

plt.subplot(132)
wykres = grupa.plot.consum()
wykres.set_ylabel('Liczba')
wykres.set_xlabel('Plec')
wykres.legend()
plt.title('liczba urodzonych chłopców i dziewczynek')
plt.show()


grupa2 = df.groupby(['Plec']).agg({'Rok':['sum']})
print(grupa2)
plt.subplot(1,3,3)
wykres = grupa2.plot.bar()
wykres.set_ylabel('Liczba')
wykres.set_xlabel('Plec')
wykres.legend()
plt.title('liczba urodzonych chłopców i dziewczynek')
plt.show()