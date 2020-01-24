from functools import reduce


with open('in.txt', 'r') as f:
    lines = f.read().split('\n')
    lines = [int(x) for x in lines if x]

res = reduce(lambda x, y: x+y, lines)

with open('out1.txt', 'w+') as f:
    f.write('Resultado: ' + str(res))
