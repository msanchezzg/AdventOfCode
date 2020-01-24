
f = open('in1.txt', 'r')
lines = f.read().split(',')
lines = [int(x) for x in lines]

i = 0
while(i < len(lines)):
    n = str(lines[i])
    opcode = n[-2:]
    params = list(n[:-2])
    npar = len(params)

    if(opcode == '99'):
        break

    elif(opcode == '01' or opcode == '1'):
        a = lines[i+1]
        b = lines[i+2]
        pos = lines[i+3]

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

        lines[pos] = a + b
        i += 4

    elif(opcode == '02' or opcode == '2'):
        a = lines[i+1]
        b = lines[i+2]
        pos = lines[i+3]

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

        lines[pos] = a * b
        i += 4

    elif(opcode == '03' or opcode == '3'):

        pos = int(lines[i+1])
        print('Entrada: ', end='')
        lines[pos] = int(input())
        print()

        i += 2

    elif(opcode == '04' or opcode == '4'):

        a = int(lines[i+1])
        if (npar == 0):
            a = lines[a]

        elif (npar > 1):
            if(params[-1] == '0'):
                a = lines[a]

        print('Diagnostic code: ' + str(a))

        i += 2

'''
f = open('out1.txt', 'w+')
f.write(str(lines))
f.close()
'''