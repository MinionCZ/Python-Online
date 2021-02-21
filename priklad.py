import random
nahodneCislo1 = random.randint(0, 100)
nahodneCislo2 = random.randint(0, 100)
print(nahodneCislo1, "+", nahodneCislo2)
vysledek = input("Vysledek:")
vysledek = int(vysledek)
soucet = nahodneCislo1 + nahodneCislo2

if vysledek == soucet:
    print("Spravně")
else:
    print("Chybně, mělo to být: ", soucet)
