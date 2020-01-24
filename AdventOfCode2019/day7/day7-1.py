from itertools import permutations


def tresParams(lista, i, params):
    a = lines[i+1]
    b = lines[i+2]
    pos = lines[i+3]
    npar = len(params)
    '''
    print('\taINI: ' + str(a))
    print('\tbINI: ' + str(b))
    print('\tposINI: ' + str(pos))
    '''

    if (npar == 0):
        a = lines[a]
        b = lines[b]
    elif (npar == 1):
        b = lines[b]
        if(params[0] == '0'):
            a = lines[a]
    elif (npar == 2):
        if(params[1] == '0'):
            a = lines[a]
        if(params[0] == '0'):
            b = lines[b]
    '''
    print('\ta: ' + str(a))
    print('\tb: ' + str(b))
    print('\tpos: ' + str(pos))
    '''

    return a, b, pos


def dosParams(lista, i, params):
    a = lines[i+1]
    b = lines[i+2]
    npar = len(params)
    '''
    print('\taINI: ' + str(a))
    print('\tbINI: ' + str(b))
    '''

    if (npar == 0):
        a = lines[a]
        b = lines[b]
    elif (npar == 1):
        b = lines[b]
        if(params[0] == '0'):
            a = lines[a]
    elif (npar == 2):
        if(params[1] == '0'):
            a = lines[a]
        if(params[0] == '0'):
            b = lines[b]
    '''
    print('\ta: ' + str(a))
    print('\tb: ' + str(b))
    '''
    return a, b


'''
    OPCODES:
        1: Sum
        2: Mul
        3: Input
        4: Print
        5: Jump if true
        6: Jump if false
        7: Less than
        8: Equals
        99: Halt
    PARAMETER MODES:
        1: Value
        0: Position
'''
def func(lines, ins):
    # print(lines)
    # print(ins)
    i = 0
    outs = []
    while(i < len(lines)):
        n = str(lines[i])
        opcode = n[-2:]
        params = list(n[:-2])
        npar = len(params)
        '''   
        print('i: ' + str(i))
        print('n: ' + str(n))
        print('opcode: ' + str(opcode))
        print('params: ' + str(params))
        '''

        if(opcode == '99'):
            break
        
        elif(opcode == '01' or opcode == '1'):
            a, b, pos = tresParams(lines, i, params)
            lines[pos] = a + b
            i += 4

        elif(opcode == '02' or opcode == '2'):
            a, b, pos = tresParams(lines, i, params)
            lines[pos] = a * b
            i += 4

        elif(opcode == '03' or opcode == '3'):
            pos = lines[i+1]
            # print('Entrada: ', end='')
            # lines[pos] = int(input())
            lines[pos] = ins[0]
            ins.pop(0)
            i += 2
            # print('\tpos: ' + str(pos))

        elif(opcode == '04' or opcode == '4'):
            a = lines[i+1]
            # print('\taINI: ' + str(a))
            if (npar == 0):
                a = lines[a]

            # print('\ta: ' + str(a))

            # print(str(a))
            outs.append(a)
            # f.write('Diagnostic code: ' + str(a))

            i += 2

        elif(opcode == '05' or opcode == '5'):
            a, b = dosParams(lines, i, params)
            i = b if(a != 0) else i + 3

        elif(opcode == '06' or opcode == '6'):
            a, b = dosParams(lines, i, params)
            i = b if(a == 0) else i + 3

        elif(opcode == '07' or opcode == '7'):
            a, b, pos = tresParams(lines, i, params)
            lines[pos] = 1 if(a < b) else 0
            i += 4

        elif(opcode == '08' or opcode == '8'):
            a, b, pos = tresParams(lines, i, params)
            lines[pos] = 1 if(a == b) else 0
            i += 4
    
    return outs


with open('in.txt', 'r') as f:
    lines = f.read().split(',')
    lines = [int(x) for x in lines]


settings = [0, 1, 2, 3, 4]
permutaciones = list(permutations(settings))
outputs = {}

for p in permutaciones:
    # print(p)
    a = p[0]
    b = p[1]
    c = p[2]
    d = p[3]
    e = p[4]

    # Amp A
    outs = func(lines, [a, 0])
    # print(outs)

    # Amp B
    outs = func(lines, [b, outs[0]])

    # Amp C
    outs = func(lines, [c, outs[0]])

    # Amp D
    outs = func(lines, [d, outs[0]])

    # Amp E
    outs = func(lines, [e, outs[0]])

    outputs[p] = outs[0]


# print(outputs)
maxOutput = max(outputs.values())
maxCombinacion = list(outputs.keys())[list(outputs.values()).index(maxOutput)]
with open('out1.txt', 'w+') as f:
    f.write('Mejor combinacion: ' + str(maxCombinacion) + '\n')
    f.write('Salida: ' + str(maxOutput))













