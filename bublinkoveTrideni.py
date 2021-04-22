seznam = []
for x in range(10000):
    seznam.append(x)
jeSeznamNesetrizen = True
while jeSeznamNesetrizen:
    jeSeznamNesetrizen = False
    for x in range(1, len(seznam)):
        if seznam[x - 1] < seznam[x]:
            a = seznam[x]
            seznam[x] = seznam[x - 1]
            seznam[x - 1] = a
            jeSeznamNesetrizen = True
print(seznam)


