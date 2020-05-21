import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel('datasets/imiona.xlsx')
print(df)

grupa = df.groupby(['Plec']).agg({'Liczba':['sum']})
print(grupa)
wykres = grupa.plot.bar()
wykres.set_ylabel('Liczba')
wykres.set_xlabel('Plec')
wykres.legend()
plt.title('liczba urodzonych chłopców i dziewczynek')
plt.show()