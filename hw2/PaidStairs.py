def foo(x, s):
	if len(s) == 1:
		return x + s[0]
	elif len(s) == 2:
		return min(s[0], s[1])
	else:
		return min(foo(s[0], s[1:]) + s[0], foo(s[1], s[2:]) + s[1])

stares = eval(input())
print(foo(0, stares))