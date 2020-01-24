import numpy as np
import copy


def getPendiente(x, y, x1, y1):
    if((x1 - x) == 0):
        return 999999999
    if((y1 - y) == 0):
        return 0
    return (y1 - y)/(x1 - x)


def getDistancia(x, y, x1, y1):
    return (x1 - x)**2 + (y1 - y)**2


def getDiccPendientes(asteroides, ast):
    asteroides2 = copy.deepcopy(asteroides)
    asteroides2.remove(ast)
    dicc_pendientes = {}

    for otro in asteroides2:
        p = getPendiente(ast[0], ast[1], otro[0], otro[1])

        if p not in dicc_pendientes:
            dicc_pendientes[p] = [otro]
        else:
            dicc_pendientes[p].append(otro)

    return dicc_pendientes


def getAsteroidesAdy(asteroides, ast):
    dicc_pendientes = {}
    total = 0
    dicc_pendientes = getDiccPendientes(asteroides, ast)

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

    return total


# Part 1
with open('in.txt', 'r') as f:
    lineas = f.read().split('\n')
    lineas = [[char for char in linea] for linea in lineas if linea]

matriz = np.array(lineas, dtype='str')
matriz = np.transpose(matriz)

i, j = np.where(matriz == '#')
asteroides = list(zip(i, j))
res = {}

for ast in asteroides:
    res[ast] = getAsteroidesAdy(asteroides, ast)

maxPuntos = max(res.values())
maxAsteroide = list(res.keys())[list(res.values()).index(maxPuntos)]


# Part 2
pendientes = getDiccPendientes(asteroides, maxAsteroide)

primerCuadrante = []
segundoCuadrante = []
tercerCuadrante = []
cuartoCuadrante = []
primero = []

for p in pendientes:
    if (p < 0):
        for punto in pendientes[p]:
            if (punto[0] >= maxAsteroide[0] and punto[1] <= maxAsteroide[1]):
                primerCuadrante.append((p, punto))
            else:
                tercerCuadrante.append((p, punto))
    else:
        for punto in pendientes[p]:
            if (punto[0] >= maxAsteroide[0] and punto[1] >= maxAsteroide[1]):
                segundoCuadrante.append((p, punto))
            else:
                cuartoCuadrante.append((p, punto))

primero = [x for x in cuartoCuadrante if x[0] == 999999999]
cuartoCuadrante = [x for x in cuartoCuadrante if x not in primero]

primero = sorted(primero,
    key=lambda x: (x[0], getPendiente(maxAsteroide[0], maxAsteroide[1], x[1][0], x[1][1])))
primerCuadrante = sorted(primerCuadrante,
    key=lambda x: (-x[0], getPendiente(maxAsteroide[0], maxAsteroide[1], x[1][0], x[1][1])))
segundoCuadrante = sorted(segundoCuadrante,
    key=lambda x: (-x[0], getPendiente(maxAsteroide[0], maxAsteroide[1], x[1][0], x[1][1])))
tercerCuadrante = sorted(tercerCuadrante,
    key=lambda x: (-x[0], getPendiente(maxAsteroide[0], maxAsteroide[1], x[1][0], x[1][1])))
cuartoCuadrante = sorted(cuartoCuadrante,
    key=lambda x: (-x[0], getPendiente(maxAsteroide[0], maxAsteroide[1], x[1][0], x[1][1])))

primero = primero[::-1]
primerCuadrante = primerCuadrante[::-1]
segundoCuadrante = segundoCuadrante[::-1]
tercerCuadrante = tercerCuadrante[::-1]
cuartoCuadrante = cuartoCuadrante[::-1]

total = primero + primerCuadrante + segundoCuadrante + tercerCuadrante + cuartoCuadrante

orden = []
astTotal = len(total)
pAnterior = 88888888888
i = 0

while(astTotal > 0):
    if (i >= astTotal):
        i = 0

    a = total[i]

    if (a[0] == pAnterior):
        if(astTotal == 1):
            orden.append(a)
            total.remove(a)
            astTotal -= 1

        elif(all(ast[0] == pAnterior for ast in total)):
            orden.append(a)
            total.remove(a)
            astTotal -= 1

        i += 1

    else:
        pAnterior = a[0]
        orden.append(a)
        total.remove(a)
        astTotal -= 1
        # i += 1


with open('out2.txt', 'w+') as f:
    f.write('Centro: ' + str(maxAsteroide) + '\n')
    f.write('Orden de impacto de los asteroides:\n')

    j = 1
    for i in orden:
        f.write('\t' + str(j) + ': ' + str(i[1]) + '\n')
        j += 1

    f.write('\n')
