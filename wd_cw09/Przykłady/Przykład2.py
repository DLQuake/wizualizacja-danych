import pandas as pd
import matplotlib.pyplot as plt


data = {'Kraj': ['Belgia',  'Indie',  'Brazylia', 'Polska'],
'Stolica': ['Bruksela',  'New Delhi',  'Brasilia', 'Warszawa'],
'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
'Populacja': [11190846, 1303171035, 207847528, 38675467]}
df = pd.DataFrame(data, columns=['Kraj',  'Stolica', 'Kontynent', 'Populacja'])
print(df)

grupa = df.groupby(['Kontynent']).agg({'Populacja':['sum']})
print(grupa)
wykres = grupa.plot.bar()
wykres.set_ylabel('Mld')
wykres.set_xlabel('Kontynent')
wykres.legend()
plt.title('Populacja z podziałem na kontynenty')
plt.show()
