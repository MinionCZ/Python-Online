vyskaPyramidy = int(input("Napiste prosim vysku:"))

pocetHvezdicek = 1
pocetMezer = vyskaPyramidy - 1

for x in range(vyskaPyramidy):
    for z in range(pocetMezer):
        print(" ", end="")
    for y in range(pocetHvezdicek):
        print("*", end="")
    print("")
    pocetHvezdicek += 2
    pocetMezer -= 1