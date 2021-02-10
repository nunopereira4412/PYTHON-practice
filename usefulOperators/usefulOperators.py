# RANGE - returns the numbers from 0 to 10 with step size of 2

for x in range(0, 10, 2):
	print(x)
	if x == 8:
		print('\n\n')

print(list(range(0, 10, 2)))


# enumerator permite fazer track ao index de uma dada letra de 
# uma string, value de uma lista, dictio

indexCount = 0
word = 'abc'

for letter in word:
	print(f'Letter at index {indexCount} is {letter}')
	indexCount += 1

indexCount = 0

for item in enumerate(word):
	print(item)

for index, letter in enumerate(word):
	print(index)
	print(letter)

l = [0, 1, 2, 3]
l2 = [10, 11, 12, 13]

for value in l2:
	l.append(value)

print(l)

# zip junta elementos de listas sob a forma de tuplos

zipResult = zip(l, l2)

for value in zipResult:
	print(value)

print('ZIP PRINT TEST: ', zipResult)

print(type(zipResult))

print(list(zipResult))
# in ve se um dado elemento exista numa lista, string, dict etc

print(4 in l)
print((1 and 4) in l)

print('S' in 'Sam')

d = {'um':1, 'dois':2}

print(1 in d.values())

l = [1, 2, 3, 4]

# min / max values

print(min(l))
print(max(l))

print(l)

# shuffle stuff

from random import shuffle

x = 0

while x < 5:
	shuffle(l)
	print(l)
	x += 1

word = 'abcd'

wordList = list(word)

print('before shuffle', wordList)

shuffle(wordList)

print('after shuffle', wordList)

word = ''.join(wordList)

print(word)

# randint

from random import randint
x = 0
while x < 5:
	y = randint(0, 10)
	print(y)
	x += 1

# input - whatever we give as input IT IS ALWAYS a string

result = input('Enter a number here: ')

# could do 
#
# result = int(input('Enter a number here: '))

print(result[0])

# result += 1 --> ERRO
# print(result[1]) --> ERROR: index out of range

i = int(result)
f = float(result)

print(f'int: {i}, float: {f}')

i += 1
f += 1

print(f'AFTER increment \n int: {i}, float: {f}')
