import math


def func(n):
	x = math.floor(n/3) - 2
	if(x < 0):
		return 0

	return x


f = open('in2.txt', 'r')
lines = f.read()
lines = lines.split('\n')
lines = [int(x) for x in lines if x]

res = 0
for n in lines:
	total = 0

	while(True):
		y = func(n)
		total += y
		if (y == 0):
			break
		n = y

	res += total


f = open('out2.txt', 'w+')
f.write(str(res))
