import networkx as nx


def getCentro(grafo, letra):
    return str(grafo[letra])


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

    grafonx = nx.from_dict_of_lists(grafo)
    camino = nx.shortest_path(grafonx, "SAN", "YOU")


with open('out2.txt', 'w+') as f:
    f.write('Camino mas corto de SAN a YOU: ' + str(camino) + '\n')
    f.write('Longitud del camino: ' + str(len(camino)) + '\n')
    f.write('Longitud del camino entre las órbitas: ' + str(len(camino) - 3))