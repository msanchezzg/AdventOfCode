
def manhattanDist(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])


# with open('prueba.in', 'r') as f:
with open('in.txt', 'r') as f:
    coords = f.read().split('\n')

dicc_letras = {}
letra = 'A'
maxx = 0
maxy = 0

for c in coords:
    x, y = c.split(',')
    x, y = int(x), int(y)
    dicc_letras[letra] = [(y, x)]
    letra = chr(ord(letra) + 1)
    if x > maxx:
        maxx = x
    if y > maxy:
        maxy = y

# Coordenadas de las casillas que estan en los bordes de la matriz
bordes = []
for i in range(maxy + 1):
    bordes.append((i, 0))
    bordes.append((i, maxx))

for i in range(maxx + 1):
    bordes.append((0, i))
    bordes.append((maxy, i))


letras = list(dicc_letras.keys())
for i in range(maxy+1):
    for j in range(maxx+1):
        minDist = 9999999
        minLetra = '.'
        dosIguales = False

        for letra in dicc_letras:
            d = manhattanDist((i, j), dicc_letras[letra][0])

            if d == 0:
                minLetra = letra
                break
            
            if d == minDist:
                dosIguales = True

            elif d < minDist:
                minDist = d
                minLetra = letra
                dosIguales = False

        if dosIguales is True:
            minLetra = '.'

        if minLetra in letras:
            dicc_letras[minLetra].append((i, j))
            if (i, j) in bordes:
                letras.remove(minLetra)


casillas = [len(dicc_letras[l])-1 for l in letras]

# with open('prueba1.out', 'w+') as f:
with open('out1', 'w+') as f:
    f.write('Máximo número de casillas adyacentes no infinitas: ' + str(max(casillas)))
