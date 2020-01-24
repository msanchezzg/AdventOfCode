import numpy as np
import copy


def getPendiente(x, y, x1, y1):
    if((x1 - x) == 0):
        return 999999999
    if((y1 - y) == 0):
        return 0
    return (y1 - y)/(x1 - x)


with open('in.txt', 'r') as f:
    lineas = f.read().split('\n')
    lineas = [[char for char in linea] for linea in lineas if linea]

matriz = np.array(lineas, dtype='str')
matriz = np.transpose(matriz)
print(matriz)

i, j = np.where(matriz == '#')
asteroides = list(zip(i, j))
res = {}

for ast in asteroides:
    asteroides2 = copy.deepcopy(asteroides)
    asteroides2.remove(ast)
    dicc_pendientes = {}
    total = 0

    for otro in asteroides2:
        p = getPendiente(ast[0], ast[1], otro[0], otro[1])

        if p not in dicc_pendientes:
            dicc_pendientes[p] = [otro]
        else:
            dicc_pendientes[p].append(otro)

    for pendiente in dicc_pendientes:
        if (len(dicc_pendientes[pendiente]) == 1):
            total += 1
        else:
            if (pendiente == 0):    # recta horizontal
                # Puntos a la izquierda
                lista1 = [punto for punto in dicc_pendientes[pendiente] if punto[0] < ast[0]]
                # Puntos a la derecha
                lista2 = [punto for punto in dicc_pendientes[pendiente] if punto[0] > ast[0]]

            else:   # recta vertical u oblicua
                # Puntos de arriba
                lista1 = [punto for punto in dicc_pendientes[pendiente] if punto[1] < ast[1]]
                # Puntos de abajo
                lista2 = [punto for punto in dicc_pendientes[pendiente] if punto[1] > ast[1]]

            if(len(lista1) >= 1):
                total += 1
            if(len(lista2) >= 1):
                total += 1

    res[ast] = total

maxPuntos = max(res.values())
maxAsteroide = list(res.keys())[list(res.values()).index(maxPuntos)]

with open('out1.txt', 'w+') as f:
    f.write('Asteroides y puntos a los que llegan:\n')
    for k, v in res.items():
        f.write(str(k) + ': ' + str(v) + '\n')

    f.write('\nAsteroide con mayor numero de puntos: ' + str(maxAsteroide) + ' - ' + str(maxPuntos))
