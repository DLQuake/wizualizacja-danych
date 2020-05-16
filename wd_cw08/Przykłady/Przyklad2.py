import pandas as pd
import numpy as np

seria = pd.Series([10, 12, 8, 14], index=['Ala', 'Marek', 'Wiesiek', 'Eleonora'])

data = {'Kraj': ['Belgia',  'Indie',  'Brazylia'],
'Stolica': ['Bruksela',  'New Delhi',  'Brasilia'],
'Populacja': [11190846, 1303171035, 207847528]}
df = pd.DataFrame(data, columns=['Kraj',  'Stolica',  'Populacja'])


# pojedynczy element Series
print(seria['Wiesiek'])
# możemy również dostać się do wartości serii jak do pola klasy
print(seria.Wiesiek)

# tak jak przy cięciu list
print(df[1:])

# kolumna po etykiecie
print(df['Populacja'])
# pojedyncza kolumna ze zbioru kolumn
print(df.ix[:, 'Stolica'])

# pobieranie pojedynczej wartości po indeksie kolumny i wiersza
print(df.iloc[[0], [0]])


# pobieranie wartości po indeksie wiersza i etykiecie kolumny
print(df.loc[[0],  ['Kraj']])
print(df.at[0, 'Kraj'])

# pojedynczy wiersz
print(df.ix[2])

# wybiera kolumnę z podanego wiersza
print(df.ix[1, 'Stolica'])

# podobnie jak w przypadku serii można odwoływać się do kolumn jak do pól klasy
# dodatkowo print jest wywoływany jak w pętli dla każdego elementu danej kolumny
print('kraj: ' + df.Kraj)

# Pandas posiada również funckje pozwalające na losowe pobieranie elementów lub
# w odniesieniu do procentowej wielkości całego zbioru

# jeden losowy element
print(df.sample())
# n losowych elementów
print(df.sample(2))
# ilość elementów procentowo - uwaga na zaokrąglanie
print(df.sample(frac=0.5))

# jeżeli potrzeba nam więcej próbek niż znajduje się w zbiorze i dopuszczamy duplikaty
# to możemy użyć parametru replace, który będzie losował z powtórzeniami
print(df.sample(n=10, replace=True))

# zamiast wyświetlać całą kolekcję możemy wyświetlić tylko określoną liczbę pierwszych lub ostatnich elementów
print(df.head())
print(df.head(2))
print(df.tail(1))

# sprawdź wartości atrybutów index, columns, values dla Series lub DataFrame
# Pandas jest też w stanie wyświetlić statystykę dla wartości, które dana kolekcja zawiera, o ile są jakieś kolumny
# z danymi numerycznymi

print(df.describe())
# transpozycja to zmienna T kolekcji, podobnie jak w Numpy
print(df.T)