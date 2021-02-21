cislo1 = int(input("Zadejte prvni cislo:"))
cislo2 = int(input("Zadejte druhe cislo:"))
cislo3 = int(input("Zadejte treti cislo:"))

if cislo1 < cislo2 and cislo1 < cislo3:
    print("Nejmensi cislo je: ", cislo1)
elif cislo2 < cislo1 and cislo2 < cislo3:
    print("Nejmensi cislo je: ", cislo2)
elif cislo3 < cislo1 and cislo3 < cislo2:
    print("Nejmensi cislo je: ", cislo3)
elif cislo3 == cislo1 and cislo3 == cislo2:
    print("Vsechna cisla jsou stejne velka")
