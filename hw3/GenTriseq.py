v = eval(input())
N = eval(input())

def gener(v):
	for i in v:
		for j in v:
			if j<=i:
				yield j

j = 0
for i in gener(v):
	if j == N:
		print(i)
		break
	j += 1