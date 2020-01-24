
def contarNumero(lista, num):
    return [i.count(num) for i in lista]


with open('in.txt', 'r') as f:
    pixeles = f.read()
    pixeles = list(pixeles)
    ancho = 25
    alto = 6
    lista2 = [pixeles[i:i+ancho] for i in range(0, len(pixeles), ancho)]
    lista2.pop()
    lista = [lista2[i:i+alto] for i in range(0, len(lista2), alto)]

    listaCeros = [sum(contarNumero(capa, '0')) for capa in lista]
    m = listaCeros.index(min(listaCeros))
    capa = lista[m]

    unos = sum(contarNumero(capa, '1'))
    doses = sum(contarNumero(capa, '2'))
    total = unos * doses


with open('out1.txt', 'w+') as f:
    f.write('Capa con menos ceros:\n\tCapa ' + str(m) + ': ' + str(capa) + '\n\n')
    f.write('Num de 1 * num de 2: ' + str(total))
