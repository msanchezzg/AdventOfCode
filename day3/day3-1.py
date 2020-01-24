
def func(listaMov, listaCasillas2):
    xactual = 0
    yactual = 0

    for mov in listaMov:
        if (mov[0] == 'R'):
            fin = int(mov[1:])
           
            for i in range(1,fin+1):
                listaCasillas2.add((xactual+i, yactual) )

            xactual += fin

        elif (mov[0] == 'L'):
            fin = int(mov[1:])

            for i in range(1, fin+1):
                listaCasillas2.add( (xactual-i, yactual) )

            xactual -= fin

        elif (mov[0] == 'U'):
            fin = int(mov[1:])
            
            for i in range(1, fin+1):
                listaCasillas2.add( (xactual, yactual+i) )

            yactual += fin

        elif (mov[0] == 'D'):
            fin = int(mov[1:])
            
            for i in range(1, fin+1):
                listaCasillas2.add( (xactual, yactual-i) )

            yactual -= fin


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

casillas11 = {(0,0)}
casillas22 = {(0,0)}

print('func lista 1...')
func(wire1, casillas11)
print('func lista 2...')
func(wire2, casillas22)

print('intersecciones...')
intersecciones = [x for x in casillas11 if x in casillas22]
print('distancias...')
intersecciones.remove((0, 0))
distancias = [distancia(x, y) for (x, y) in intersecciones]
# distancias.remove(0)
minimaDis = min(distancias)

f = open('out1c.txt', 'w+')
f.write('Puntos en comun: ' + str(intersecciones) + '\n')
f.write('Distancias de cada punto: ' + str(distancias) + '\n')
f.write('Minima distancia: ' + str(minimaDis))
