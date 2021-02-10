def hello(name):
	return 'hello ' + name

	# OR f'hello {name}''

def helloCaps(name = 'NAME'):
	return 'hello ' + name

def addN(x, y):
	'''
	DOCSTRING: Adds 2 numbers and returns the result
	'''
	return x + y

s = hello('world')

print(s)

print(addN(2, 6))

# help(addN)

print(helloCaps('world'))
print(helloCaps())

def dogCheck(s):
	'''
	Checks if the string passed as argument containts the word 'dog' 
	'''
	return 'dog' in s.lower()

print(dogCheck('there is a Dog in this string'))

print(dogCheck('this string regular'))

# help(dogCheck)
