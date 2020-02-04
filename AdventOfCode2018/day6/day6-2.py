
def manhattanDist(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])


# with open('prueba.in', 'r') as f:
with open('in.txt', 'r') as f:
    coords = f.read().split('\n')

dicc_letras = {}
letra = 'A'
maxx = 0
maxy = 0
region = []
TAMANO = 10000    # 32 en prueba.in

for c in coords:
    x, y = c.split(',')
    x, y = int(x), int(y)
    dicc_letras[letra] = [(y, x)]
    letra = chr(ord(letra) + 1)
    if x > maxx:
        maxx = x
    if y > maxy:
        maxy = y


for i in range(maxy+1):
    for j in range(maxx+1):
        manhattan = [manhattanDist((i, j), dicc_letras[letra][0]) for letra in dicc_letras]
        if sum(manhattan) < TAMANO:
            region.append((i, j))


# with open('prueba2.out', 'w+') as f:
with open('out2', 'w+') as f:
    f.write('Tamaño de la región con distancia total < ' + str(TAMANO) + ': ' + str(len(region)))