
def getPosiciones(xini, yini, dx, dy):
    lista = []
    for i in range(xini, xini+dx):
        for j in range(yini, yini+dy):
            lista.append((i, j))

    return lista


with open('in.txt', 'r') as f:
    lines = f.read().split('\n')

pos_todas = set()
pos_repetidas = set()

for l in lines:
    pos, desp = l.split('@ ')[-1].split(': ')
    pos = pos.split(',')
    desp = desp.split('x')
    posiciones = getPosiciones(int(pos[0]), int(pos[1]), int(desp[0]), int(desp[1]))

    for p in posiciones:
        if p in pos_todas:
            if p not in pos_repetidas:
                pos_repetidas.add(p)
        else:
            pos_todas.add(p)

with open('out1.txt', 'w+') as f:
    f.write('Posiciones repetidas: ' + str(len(pos_repetidas)) + '\n')
    for x in pos_repetidas:
        f.write(str(x) + '\n')
