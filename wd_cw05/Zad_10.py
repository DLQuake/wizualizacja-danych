import itertools

kombinacje = list(itertools.combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
print(kombinacje)
print('liczba kombinacji:', len(kombinacje))