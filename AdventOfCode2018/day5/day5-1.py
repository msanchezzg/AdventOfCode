from string import ascii_lowercase


def reaction(line):
    match = True
    while match:
        match = False
        for c in ascii_lowercase:
            string = c + c.upper()
            line2 = line.replace(string, '')
            if len(line) != len(line2):
                match = True
            
            line = line2.replace(string[::-1], '')
            if len(line) != len(line2):
                match = True

            if c == 'z' and match is False:
                break
            
    return line


# with open('prueba.in', 'r') as f:
with open('in.txt', 'r') as f:
    line = f.read()

line = reaction(line)

# with open('prueba1.out', 'w+') as f:
with open('out1', 'w+') as f:
    f.write('Longitud: ' + str(len(line)) + '\n')
    f.write(line)