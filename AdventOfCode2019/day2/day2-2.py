
def func(lines):
    i = 0
    while(i < len(lines)):
        n = lines[i]

        if(n == 99):
            break

        elif(n == 1):
            a = lines[lines[i+1]]
            b = lines[lines[i+2]]
            pos = lines[i+3]

            lines[pos] = a + b

        elif(n == 2):
            a = lines[lines[i+1]]
            b = lines[lines[i+2]]
            pos = lines[i+3]

            lines[pos] = a * b
                 
        i += 4


for x in range(100):
    for y in range(100):
        f = open('in.txt', 'r')
        lines = f.read()
        lines = lines.split(',')
        lines = [int(x) for x  in lines if x]
        f.close()

        lines[1] = x
        lines[2] = y

        func(lines)

        if(lines[0] == 19690720):
            break

    if(lines[0] == 19690720):
        break


f = open('out2.txt', 'w+')
f.write(str(lines))
f.write('\n\n' + str(x) + ' ' + str(y))
f.close()
