import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

df = pd.read_excel('datasets/imiona.xlsx')
grupa = df.groupby(['Plec']).agg({'Liczba':['sum']})
# wykres kołowy z wartościami procentowymi sformatowanymi z dokładnością do 2 miejsc po przecinku
# figsize ustawia wielkość wykresu w calach, domyślnie [6.4, 4.8].
wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6))
plt.title('liczba urodzonych chłopców i dziewczynek')
plt.show()