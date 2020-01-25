import networkx as nx 


# with open('prueba', 'r') as f:
with open('in.txt', 'r') as f:
    lines = f.read().split('\n')


grafo = nx.DiGraph()

for l in lines:
    l = l.split(' ')
    a = l[1]
    b = l[7]

    grafo.add_node(a)
    grafo.add_node(b)
    grafo.add_edge(a, b)


camino = list(nx.lexicographical_topological_sort(grafo))
res = ''.join(camino)

# with open('prueba1.out', 'w+') as f:
with open('out1', 'w+') as f:
    f.write('Orden topológico: ' + res + '\n')
