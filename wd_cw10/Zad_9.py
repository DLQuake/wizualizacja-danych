import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('datasets/zamowienia.csv', delimiter=';')
print(df)

grupa=df.groupby(['Sprzedawca']).agg({'idZamowienia':['count']})
grupa.plot.pie()
plt.setp(grupa, size=14, weight="bold")
plt.title('ilość złożonych zamówień przez poszczególnych sprzedawców')
plt.legend(title='Sprzedawca')
plt.show()