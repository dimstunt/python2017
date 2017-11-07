stares = eval(input())
result = [0 for i in stares]
result[0:2] = stares[0:2]
for i in range(2, len(stares)):
	result[i] = min(result[i-1], result[i-2]) + stares[i]
print(result[-1])
