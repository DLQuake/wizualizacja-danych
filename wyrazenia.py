def wyrazenia():
    import math
    a=math.e
    b=10
    print("e^10 = ",a**b)
   

    f=5
    i=8 # pi*2/45 = 8
    logarytmnaturalny=math.log(f+math.pow(math.sin(math.pi*2/45),2))
    print("Pierwiastek 6 stopnia z Ln(",f,"+(sin(",i,"))^2) wynosi ",logarytmnaturalny**(1/6))

    c=3.55
    print("|",c,"| = ",math.fabs(c))

    d=4.80
    print("|",d,"| = ",math.fabs(d))
wyrazenia()
