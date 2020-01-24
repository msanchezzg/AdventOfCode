

def func(listaMov, listaCasillas2, recorrido, listaPasos):
    xactual = 0
    yactual = 0
    pasos = 0

    for mov in listaMov:
        if (mov[0] == 'R'):
            fin = int(mov[1:])       
            
            for i in range(1, fin+1):
                listaCasillas2.add((xactual+i, yactual) )
                recorrido.append( (xactual+i, yactual))
                listaPasos.append(pasos+i)

            xactual += fin
            pasos += fin

        elif (mov[0] == 'L'):
            fin = int(mov[1:])
            
            for i in range(1, fin+1):
                listaCasillas2.add( (xactual-i, yactual) )
                recorrido.append( (xactual-i, yactual))
                listaPasos.append(pasos+i)

            xactual -= fin
            pasos += fin

        elif (mov[0] == 'U'):
            fin = int(mov[1:]) 
            
            for i in range(1, fin+1):
                listaCasillas2.add( (xactual, yactual+i) )
                recorrido.append( (xactual, yactual+i))
                listaPasos.append(pasos+i)

            yactual += fin
            pasos += fin

        elif (mov[0] == 'D'):
            fin = int(mov[1:])
                      
            for i in range(1, fin+1):
                listaCasillas2.add( (xactual, yactual-i) )
                recorrido.append( (xactual, yactual-i))
                listaPasos.append(pasos+i)

            yactual -= fin
            pasos += fin


def distancia(x, y):
    return abs(x) + abs(y)


f = open('in.txt', 'r')
lines = f.read()
f.close()
lines = lines.split('\n')
wire1 = lines[0]
wire1 = wire1.split(',')
wire2 = lines[1]
wire2 = wire2.split(',')

casillas11 = {(0, 0)}
casillas22 = {(0, 0)}
recorrido1 = []
pasos1 = []
recorrido2 = []
pasos2 = []


print('func lista 1...')
func(wire1, casillas11, recorrido1, pasos1)
print('func lista 2...')
func(wire2, casillas22, recorrido2, pasos2)


print('intersecciones...')
intersecciones = [x for x in casillas11 if x in casillas22]
intersecciones.remove((0, 0))
print('distancias...')
distancias = [distancia(x, y) for (x, y) in intersecciones]
minimaDis = min(distancias)

casillas11 = list(casillas11)
casillas22 = list(casillas22)
pasos = []

for x, y in intersecciones:
    i1 = recorrido1.index((x, y))
    i2 = recorrido2.index((x, y))
    pasos.append(pasos1[i1]+pasos2[i2])

minimosPasos = min(pasos)


f = open('out3c.txt', 'w+')
f.write('Puntos en comun: ' + str(intersecciones) + '\n')
f.write('Pasos de cada punto: ' + str(pasos) + '\n')
f.write('Minimos pasos: ' + str(minimosPasos))
