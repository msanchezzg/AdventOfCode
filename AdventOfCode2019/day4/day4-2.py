
def ordenado(lista):
    return all(lista[i] <= lista[i+1] for i in range(len(lista)-1))


def adyacente(lista):
    parcial = []
    total = []

    i = 0
    while(i < len(lista)):
        n = lista[i]

        while(i < len(lista) and lista[i] == n):
            parcial.append(n)
            i += 1

        total.append(parcial)
        parcial = []

    return any(len(parcial) == 2 for parcial in total)


f = open('in.txt', 'r')
lines = f.read()
f.close()

lines = lines.split('-')
ini = lines[0]
fin = lines[1]
total = 0

for i in range(int(ini), int(fin)+1):
    if (not ordenado(list(str(i)))):
        continue

    if (not adyacente(list(str(i)))):
        continue

    total += 1


f = open('out2.txt', 'w+')
f.write('Total parte 2: ' + str(total))
