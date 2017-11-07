a = eval(input())
if not len(a)%2:
	print(a[-2::-2]+ a[1::2])
else:
	print(a[::-2] + a[1::2])