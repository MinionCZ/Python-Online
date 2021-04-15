textNaSifrovani = input("Text na zasifrovani:")
posun = int(input("Zadejte cislo od 0 do 26:"))

def overVstup(textNaSifrovani, posun):
    if posun < 0 or posun > 26:
        return False
    for pismenko in textNaSifrovani:
        if not (ord(pismenko) >= ord("a") and ord(pismenko) <= ord("z")) and pismenko != ' ':
            return False
    return True

def posunText(textNaSifrovani, posun):
    posunutyText = ""
    for pismenko in textNaSifrovani:
        if pismenko == ' ':
            posunutyText += " "
            continue

        pismenko = ord(pismenko) + posun
        if pismenko <= ord("z"):
            posunutyText += chr(pismenko)
        else:
            pos = pismenko - ord("z")
            pismenko = ord("a") + pos
            posunutyText += chr(pismenko)
    return posunutyText

if overVstup(textNaSifrovani, posun):
    print(posunText(textNaSifrovani, posun))
else:
    print("Nespravny vstup")
