#Napisz pierwszy skrypt, w którym zadeklarujesz po dwie zmienne każdego typu a następnie wyświetl te zmienne
def zad_1():
    a = 1
    b = "abc"

    print(a, b)
    print("\n-----------------------------\n")
    int1 = 10
    int2 = 123456789

    float1, float2 = 3.1415, -0.121

    complex1 = 1 + 1j
    complex2 = 2 - 3j

    string1 = 'Cos tam'
    string2 = 'jajo'
    print('int:', int1, int2)
    print('float:', float1, float2)
    print('complex:', complex1, complex2)
    print('string:', string1, string2)
# wywolane zadan
zad_1()