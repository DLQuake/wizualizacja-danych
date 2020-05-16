import pandas as pd
import numpy as np

seria = pd.Series([10, 12, 8, 14], index=['Ala', 'Marek', 'Wiesiek', 'Eleonora'])

data = {'Kraj': ['Belgia',  'Indie',  'Brazylia'],
'Stolica': ['Bruksela',  'New Delhi',  'Brasilia'],
'Populacja': [11190846, 1303171035, 207847528]}
df = pd.DataFrame(data, columns=['Kraj',  'Stolica',  'Populacja'])

# wyświetla dane z serii gdzie wartość większa od 1
print(seria[(seria > 1)])
# nieco inny efekt można osiągnąć wykorzystując funkcję where, która zwraca kolekcję w oryginalnej wielkości (liczebności)
# elementów, ale wartości nie spełniające warunku uzupełnia wartością NaN
print(seria.where(seria > 10))
# możemy również podać wartość, która zostanie podstawiona zamiast NaN
print(seria.where(seria > 10, 'za duze'))
# jeszcze inna własność where pozwala na modyfikowanie oryginalnego zbioru (domyślnie zwaracana jest kopia)
seria2 = seria.copy()
seria2.where(seria2 > 10, 'za duze', inplace=True)
print('############')
print(seria2)

# wyświetla dane z serii gdzie wartość nie jest większa od 10
print(seria[~(seria > 10)])
# warunki możemy ze sobą łączyć
print(seria[(seria < 13) & (seria > 8)])

# warunki pobierania danych dla DataFrame
print(df[df['Populacja']>1200000000])
# bardziej skomplikowane warunki
print(df[((df.Populacja > 1000000) & (df.index.isin([0,2])))])

# inny przykład z listą dopuszczalnych wartości oraz isin zwracająca wartości boolowskie
print('######')
szukaj = ['Belgia', 'Brasilia']
print(df.isin(szukaj))


# zmiana, usuwanie i dodawanie danych

# w przypadku serii możemy dodać/zmienić wartość poprzez odwołanie się do elementu serii przez klucz (indeks)
seria['Wiesiek'] = 15
print(seria.Wiesiek)
seria['Alan'] = 16
print(seria)

# podobna operacja dla DataFrame ma nieco inny efekt - wartość ustawiona dla wszystkich kolumn
df.loc[4] = 'dodane'
print(df)
# ale można dodać wiersz w postaci listy
df.loc[5] = ['Polska', 'Warszawa', 38675467]
print(df)

# usuwanie danych można wykonać przez funkcję drop, ale pamiętajmy, że operacja nie wykonuje się in-place więc
# zwracana jest kopia DataFrame z usuniętymi wartościami
new_df = df.drop([4])
print(new_df)
# więc jeżeli chcemy zmienić pierwotny zbiór dodajemy parametr inplace=True
df.drop([4], inplace=True)
# można usuwać również całe kolumny po nazwie indeksu, ale wykonanie tej komendy uniemożliwi
# wykonanie dalszego kodu (można przetstować po zakomentowaniu dalszej części listingu)
# df.drop('Kraj', axis=1, inplace=True)
print(df)

# do DataFrame możemy dodawać również kolumny zamiast wierszy
df['Kontynent'] = ['Europa', 'Azja', 'Ameryka Południowa', 'Europa']
print(df)

# Pandas ma również własne funkcje sortowania danych
print(df.sort_values(by='Kraj'))

# grupowania
grouped = df.groupby(['Kontynent'])
print(grouped.get_group('Europa'))
# można też jak w SQL czy Excelu uruchomić funkcje agregujące na danej kolumnie
print(df.groupby(['Kontynent']).agg({'Populacja':['sum']}))
# więcej przykładów można znaleźć pod adresem https://pandas.pydata.org/pandas-docs/stable/generated/pandas.core.groupby.DataFrameGroupBy.agg.html

# podobny mechanizm to sumy częściowe i tabele przestawne znane z Excela, które w Pandas również mają swoje odpowiedniki
print("_____ sumy częściowe ______")
tabela = pd.pivot_table(df,values=['Populacja'],index=['Kontynent'],columns=['Kraj'],aggfunc=np.sum,margins=True)
print(tabela.stack('Kraj'))