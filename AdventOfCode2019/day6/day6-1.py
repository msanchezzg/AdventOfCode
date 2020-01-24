
def contarOrbitas(grafo, letra):
    if (len(grafo[letra]) == 0):
        return 0
    
    else:
        return len(grafo[letra]) + sum([contarOrbitas(grafo, l) for l in grafo[letra]])


with open('in.txt', 'r') as f:
    lines = f.read().split('\n')
    lines = [x for x in lines if x]
    grafo = {'COM': []}
    total = 0

    for linea in lines:
        linea = linea.split(')')
        centro = linea[0]
        orb = linea[1]

        if (orb in grafo):
            grafo[orb].append(centro)

        else:
            grafo[orb] = [centro]

    for planeta in grafo:
        total += contarOrbitas(grafo, planeta)


with open('out1.txt', 'w+') as f:
    f.write('Orbitas totales: ' + str(total))
