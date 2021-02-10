v = [1, 2, 3, 5, 6, 7, 8]

def square(number):
	return number**2

print(list(map(square, v)))

def splitOnA(word):
	return word.split('a')

words = ['1111', 'um', 'tres', 'quatro', 'rr a ']

print(list(map(splitOnA, words)))

def checkEven(num):
	return num % 2 == 0

print(list(filter(checkEven, v)))

#curiosity

print(list(map(checkEven, v)))

print(list(map(lambda v : v % 2 == 0, v)))

print(list(filter(lambda v : v % 2 == 0, v)))

l = ['um', 'dois', 'tres', 'quatro']

print(list(map(lambda word : word[::-1], l)))

l2 = []

for word in l:
	l2.append(word[::-1])

print(l2)
