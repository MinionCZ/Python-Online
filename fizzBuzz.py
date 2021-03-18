#1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 ...
def overVstup(vstup):
    mnozinaCisel = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
    for znak in vstup:
        if not znak in mnozinaCisel:
            print("Zadal jsi špatné číslo")
            return -1
    return int(vstup)

vstup = input("Zadej celé kladné číslo:")
maxPocet = overVstup(vstup)

if maxPocet == -1:
    exit()

maxPocet += 1

for cislo in range(1, maxPocet):
    if cislo % 5 == 0 and cislo % 3 == 0:
        print("FizzBuzz")
    elif cislo % 5 == 0:
        print("Buzz")
    elif cislo % 3 == 0:
        print("Fizz")
    else:
        print(cislo)
