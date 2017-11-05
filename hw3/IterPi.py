def pigen():
    pi = 0
    index = -1
    sub = -4
    while True:
        index += 2
        sub *= -1
        pi += sub/index
        yield pi

eps = eval(input())
k2 = 0
i = 0

for k1 in pigen():
    if abs(k2 - k1) <= eps:
        break
    k2 = k1
    i += 1

print(i)