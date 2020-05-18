import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dane.csv', delimiter=';')
grupa = df.groupby(['Imię i nazwisko']).agg({'Wartość zamówienia':['sum']})
# wykres kołowy z wartościami procentowymi sformatowanymi z dokładnością do 2 miejsc po przecinku
# figsize ustawia wielkość wykresu w calach, domyślnie [6.4, 4.8].
wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6))
plt.title('Suma zamównień dla sprzedawcy')
plt.show()