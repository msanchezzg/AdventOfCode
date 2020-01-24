def unaDiferencia(a, b):
    difs = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            difs += 1
        if difs > 1:
            return False

    if difs == 1:
        return True

    return False


with open('in.txt', 'r') as f:
    lines = f.read().split('\n')

encontrado = False

for l in lines:
    for l2 in lines:
        if unaDiferencia(l, l2):
            encontrado = True
            break

    if encontrado:
        break


comunes = ''.join([x for x in l if x in l2])
with open('out2', 'w+') as f:
    f.write('IDs: ' + str(l) + ' - ' + str(l2) + '\n')
    f.write('Letras comunes: ' + str(comunes) + '\n')
