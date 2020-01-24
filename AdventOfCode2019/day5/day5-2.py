
def tresParams(lista, i, params):
    a = lines[i+1]
    b = lines[i+2]
    pos = lines[i+3]
    npar = len(params)

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

    return a, b, pos


def dosParams(lista, i, params):
    a = lines[i+1]
    b = lines[i+2]
    npar = len(params)

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

    return a, b


with open('in1.txt', 'r') as f:
    lines = f.read().split(',')
    lines = [int(x) for x in lines]
    i = 0

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

with open('out2.txt', 'w+') as f:
    while(i < len(lines)):
        n = str(lines[i])
        opcode = n[-2:]
        params = list(n[:-2])
        npar = len(params)

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
            print('Entrada: ', end='')
            lines[pos] = int(input())
            i += 2

        elif(opcode == '04' or opcode == '4'):
            a = lines[i+1]
            if (npar == 0):
                a = lines[a]

            # print(str(a))
            f.write('Diagnostic code: ' + str(a))
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
