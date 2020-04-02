#Utwórz słownik z produktami spożywczymi do kupienia. Klucz to niech będzie nazwa produktu a
#wartość - jednostka w jakiej się je kupuje (np. sztuki, kg itd.). Wykorzystaj Python Comprehension do
#zdefiniowania nowej listy, gdzie będą produkty, których wartość to sztuki.
slownik = {'jabłka': 'kg','sok pomarańczowy': 'opakowanie','woda': 'butelka',}

odwrocony_slownik = {value: key for key, value in slownik.items()}

print('Oryginalny słownik:')
print(slownik)

print('Odwrócony słownik:')
print(odwrocony_slownik)