with open('in.txt', 'r') as f:
    lines = f.read().split('\n')
    # For tests
    # lines = f.read().split(',')
    lines = [int(x) for x in lines if x]

n = 0
freqs = set()
freqs.add(0)
encontrado = False

with open('out2.txt', 'w+') as f:
    while not encontrado:
        for fr in lines:
            n += fr
            if n in freqs:
                encontrado = True
                break

            freqs.add(n)

    f.write('Primera frecuencia repetida: ' + str(n))
