from math import log
num = eval(input())
cell = 2
while cell ** 2 <= num:
	if log(num, cell) % 1 == 0:
		print('YES')
		break
	cell+=1
else:
	print('NO')