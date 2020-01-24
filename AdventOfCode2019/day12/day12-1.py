
class Luna:
    def __init__(self):
        self.velocidad = Velocidad()
        self.posicion = Posicion()
    
    def __repr__(self):
        s = 'pos= <'
        s += 'x=' + str(self.posicion.x) + ', '
        s += 'y=' + str(self.posicion.y) + ', '
        s += 'z=' + str(self.posicion.z) + '>, vel= <'
        s += 'x=' + str(self.velocidad.x) + ', '
        s += 'y=' + str(self.velocidad.y) + ', '
        s += 'z=' + str(self.velocidad.z) + '>'

        return s

    @property
    def posicion(self):
        return self.__posicion

    @posicion.setter
    def posicion(self, posicion):
        self.__posicion = posicion

    def energiaCin(self):
        return abs(self.velocidad.x) + abs(self.velocidad.y) + abs(self.velocidad.z)

    def energiaPot(self):
        return abs(self.posicion.x) + abs(self.posicion.y) + abs(self.posicion.z)

    def energiaTotal(self):
        return self.energiaPot() * self.energiaCin()

    def cambiarVelocidad(self, luna):
        if (luna.posicion.x > self.posicion.x):
            self.velocidad.x += 1
        elif (luna.posicion.x < self.posicion.x):
            self.velocidad.x -= 1

        if (luna.posicion.y > self.posicion.y):
            self.velocidad.y += 1
        elif (luna.posicion.y < self.posicion.y):
            self.velocidad.y -= 1

        if (luna.posicion.z > self.posicion.z):
            self.velocidad.z += 1
        elif (luna.posicion.z < self.posicion.z):
            self.velocidad.z -= 1

    def cambiarPosicion(self):
        self.posicion.x += self.velocidad.x
        self.posicion.y += self.velocidad.y
        self.posicion.z += self.velocidad.z


class Velocidad:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z


class Posicion:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z


###########main
with open('in.txt', 'r') as f:
    lines = f.read().split('\n')

lunas = []
iteraciones = 1000

for i in lines:
    pos = i[:-1].split(',')
    x, y, z = [int(x.split('=')[1]) for x in pos]
    luna = Luna()
    luna.posicion = Posicion(x, y, z)
    lunas.append(luna)


with open('out1.txt', 'w+') as f:
    for i in range(iteraciones):
        for l in lunas:
            for l2 in lunas:
                l.cambiarVelocidad(l2)

        for l in lunas:
            l.cambiarPosicion()

        f.write('iteracion ' + str(i+1) + '\n')
        for l in lunas:
            f.write('\t' + str(l) + '\n')

    energia = sum([l.energiaTotal() for l in lunas])
    f.write('\nEnergía total: ' + str(energia))