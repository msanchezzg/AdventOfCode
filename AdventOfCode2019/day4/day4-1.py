
def ordenado(lista):
    return all(lista[i] <= lista[i+1] for i in range(len(lista)-1))


def adyacente(lista):
    return any(lista[i] == lista[i+1] for i in range(len(lista)-1))


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


f = open('out1.txt', 'w+')
f.write('Total parte 1: ' + str(total))
