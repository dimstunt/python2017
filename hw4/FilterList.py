a = eval(input())
M, N = eval(input())
result = []
for i in range(len(a)):
	if a[i] % N != 0 and i % M != 0:
		result.append(a[i])
print(result)