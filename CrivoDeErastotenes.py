import math

n = input()
crivo = list()
aux = list()
temp = list()
cNumber = 3
countUntil = int(math.sqrt(n))

for i in range(3, n+1, 2):
    crivo.append(i)
    aux.append(i)
print crivo
print countUntil

while cNumber < countUntil:
    print cNumber, cNumber**2, aux.index(cNumber**2)
    for i in range(cNumber**2, n+1, cNumber * 2):
        if i in crivo:
            crivo.pop(crivo.index(i))
        temp.append(i)
    print temp
    print crivo
    cNumber = crivo[crivo.index(cNumber) + 1]
    temp = []
crivo.insert(0,2)
print crivo


