import pandas as pd
import xlrd
import openpyxl

df = pd.read_excel('datasets/imiona.xlsx')
print(df)
df.to_excel('Do_Zad_1.xlsx',  sheet_name='Zadanie 1')