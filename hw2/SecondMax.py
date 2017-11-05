a = eval(input())
max2 = max1 = a[0]
flag = False
for d in a:
	if max1 < d:
		max2 = max1
		max1 = d
		flag = True
	elif d>max2 and d<max1 and d>c:
		max2 = d
if flag:
	print(max2)
else:
	print('NO')