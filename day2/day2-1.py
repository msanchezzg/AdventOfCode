
f = open('in.txt', 'r')
lines = f.read().split(',')
lines = [int(x) for x in lines]

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

f = open('out.txt', 'w+')
f.write(str(lines))
f.close()
