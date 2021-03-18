def vypisNasobky(cislo): # cislo = 2, 2 * 1, 2 * 2 2 * 3 2 * 4 ... 
    zasobnik = ""
    for x in range(1, 11): # x < 11
        zasobnik += str(x * cislo)
        zasobnik += " "
    print(zasobnik)

#nacteneCislo = int(input("Napis cislo: "))
#while nacteneCislo != 0:
#    vypisNasobky(nacteneCislo)
#    nacteneCislo = int(input("Napis cislo: "))

for x in range (1, 11):
    vypisNasobky(x)

    


