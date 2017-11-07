x, y, r = eval(input())
r*=r
a, b = 1, 1
while a|b:
    a, b = eval(input())
    if not a|b:
        print('YES')
        break
    if (x - a) ** 2 + (y - b) ** 2 > r:
        print('NO')
        break
else:
    print('YES')

