def iloczyn_elementow_ciagu(* liczby):
    if len(liczby)==0:
        return 0.0
    else:
        iloczyn=1.0
        for i in liczby:
            iloczyn*=i

        return iloczyn

print("Iloczyn elementow ciagu gdy nie ma elementow wynosi ",iloczyn_elementow_ciagu())

print("iloczyn elementow ciagu (1,2,3,4,5,6,7,8) wynosi ",iloczyn_elementow_ciagu(1,2,3,4,5,6,7,8))