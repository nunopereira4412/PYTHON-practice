vec = [-2, -3, pow(2, 10)]

def add():
	return sum(vec)

def add3Args(a, b, c=0):
	return sum((a, b, c))

def addArgs(*args):
	return sum(args)

print(add())

print(abs(add()))

print(add3Args(1, 2, 3))

print(add3Args(1, 2))

print(addArgs(1, 2, 3, 5, 6, 7,8 ,43,22 ,2,23, 3, 4,44, 4, 4, 3))

def argsTest(*args):
	for arg in args:
		print(arg)

argsTest(1, 2, 3, 6, 'a', 'sdfssubl')

argsTest()
