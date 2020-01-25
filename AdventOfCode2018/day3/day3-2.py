
def getPosiciones(xini, yini, dx, dy):
    lista = []
    for i in range(xini, xini+dx):
        for j in range(yini, yini+dy):
            lista.append((i, j))

    return lista


with open('in.txt', 'r') as f:
    lines = f.read().split('\n')

dicc_pos = {}
ids = []
ids2 = []

for l in lines:
    l = l.split('@ ')
    id = int(l[0][1:])
    ids.append(id)
    ids2.append(id)
    pos, desp = l[-1].split(': ')
    pos = pos.split(',')
    desp = desp.split('x')
    posiciones = getPosiciones(int(pos[0]), int(pos[1]), int(desp[0]), int(desp[1]))
    dicc_pos[id] = posiciones


for i in ids:
    for i2 in ids:
        if i == i2:
            continue

        pos1 = set(dicc_pos[i])
        pos2 = set(dicc_pos[i2])

        res = pos1.intersection(pos2)
        if len(res) > 0:
            ids2.remove(i)
            break


with open('out2.txt', 'w+') as f:
    f.write('ID que no repite posiciones: ' + str(ids2[0]) + '\n')
