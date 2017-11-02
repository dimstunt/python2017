num = eval(input())
num2 = num
result = True
count = 0
while num2 > 0:
	count += 1
	num2 //= 10
for i in range(count//2):
	result *= (num // (10 ** i)) % 10 == num // (10 ** (count-i-1)) % 10
if result:
	print('YES')
else:
	print('NO')