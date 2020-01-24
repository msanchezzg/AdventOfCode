from PIL import Image


with open('in.txt', 'r') as f:
    pixeles = list(f.read())
    ancho = 25
    alto = 6
    lista = [pixeles[i:i+ancho] for i in range(0, len(pixeles), ancho)]
    lista.pop()
    lista = [lista[i:i+alto] for i in range(0, len(lista), alto)]
    numCapas = len(lista)

res = lista[0]
for capa in lista:
    for i in range(alto):
        for j in range(ancho):
            if (res[i][j] == '2'):
                res[i][j] = capa[i][j]

# Crear imagen
im = Image.new('1', (ancho, alto))
for i in range(alto):
    for j in range(ancho):
        im.putpixel((j, i), int(res[i][j]))

im.save('out.png')

with open('out2.txt', 'w+') as f:
    f.write('Mensaje: \n')
    for linea in res:
        for i in linea:
            f.write(' ') if i == '0' else f.write('*')
        f.write('\n')
