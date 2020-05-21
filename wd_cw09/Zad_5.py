import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/zamowienia.csv', delimiter=';')
print(df)

grupa = df.groupby(['Sprzedawca']).agg({'idZamowienia':['count']})
print(grupa)
wykres = grupa.plot.bar()
wykres.set_ylabel('Ilość zamówień')
wykres.set_xlabel('Sprzedawcy')
wykres.legend()
plt.title('ilość złożonych zamówień przez poszczególnych sprzedawców')
plt.show()