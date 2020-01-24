from collections import Counter

with open('in.txt', 'r') as f:
    lines = f.read().split('\n')

# [dos, tres]
res = [0, 0]

for l in lines:
    c = Counter(l)
    if any(v == 2 for k, v in c.items()):
        res[0] += 1

    if any(v == 3 for k, v in c.items()):
        res[1] += 1

dos, tres = res
with open('out1', 'w+') as f:
    f.write('Número de caracteres repetidos 2 veces: ' + str(dos) + '\n')
    f.write('Número de caracteres repetidos 3 veces: ' + str(tres) + '\n')
    f.write('Checksum: ' + str(dos * tres))
