slovnikMorseovky = {
    "a" : ".-",
    "b" : "-...",
    "c" : "-.-.",
    "d" : "-..",
    "e" : ".",
    "f" : "..-.",
    "g" : "--.",
    "h" : "....",
    "i" : "..",
    "j" : ".---",
    "k" : "-.-",
    "l" : ".-..",
    "m" : "--",
    "n" : "-.",
    "o" : "---",
    "p" : ".--.",
    "q" : "--.-",
    "r" : ".-.",
    "s" : "...",
    "t" : "-",
    "u" : "..-",
    "v" : "...-",
    "w" : ".--",
    "x" : "-..-",
    "y" : "-.--",
    "z" : "--..",
    " " : "",
    "." : "//"
}



textNaPrelozeni = input("Text na prelozeni: ")
textNaPrelozeni = textNaPrelozeni.lower()
zasobnik = ""

if len(textNaPrelozeni) != 0:
    pocitadlo = 0
    for pismenko in textNaPrelozeni:
        if pocitadlo < len(textNaPrelozeni) - 1:
            zasobnik += slovnikMorseovky[pismenko] + "/"
        else:
            zasobnik += slovnikMorseovky[pismenko]
        pocitadlo += 1

print(zasobnik)

