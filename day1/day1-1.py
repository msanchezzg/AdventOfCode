import math

f = open('in1.txt', 'r')
lines = f.read()
lines = lines.split('\n')
lines = [int(x) for x in lines if x]
f.close()

total = 0
for n in lines:
    x = math.floor(n/3) - 2
	total += x

f = open('out1.txt', 'w+')
f.write(str(total))
