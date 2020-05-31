import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

xlsx = pd.ExcelFile('datasets/imiona.xlsx')
df = pd.read_excel(xlsx, 'Arkusz1')
dane_wyk_1 = df.groupby(['Plec']).agg({'Liczba': 'sum'}).reset_index()
dane_wyk_2 = df.groupby(['Plec', 'Rok']).agg({'Liczba': 'sum'}).reset_index()
dane_wyk_3 = df.groupby(['Rok']).agg({'Liczba': 'sum'}).reset_index()

plt.subplot(3,1,1)
plt.bar(dane_wyk_1['Plec'], dane_wyk_1['Liczba'])


plt.subplot(3,1,2)
plt.plot(dane_wyk_2['Rok'].unique(), dane_wyk_2[dane_wyk_2['Plec'] == 'K']['Liczba'], label='Kobiety')
plt.plot(dane_wyk_2['Rok'].unique(), dane_wyk_2[dane_wyk_2['Plec'] == 'M']['Liczba'], label='Mężczyżni')
plt.legend()

plt.subplot(3,1,3)
plt.bar(dane_wyk_3['Rok'], dane_wyk_3['Liczba'])
plt.show()