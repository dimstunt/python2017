x1, y1, x2, y2, x3, y3, x4, y4 = eval(input())
if((x2-x1)*(y4-y3) == (x4-x3)*(y2-y1)):
	print('YES')
else:
	print('NO')