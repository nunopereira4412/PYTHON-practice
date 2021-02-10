s = 'abc'

l = []

for letter in s:
	l.append(letter)

print(l)

print(list(range(0, 11)))

print(l)

l = [num + 10 for num in range(0, 5)]

print(l)

l = [letter for letter in s]

print(l)

l = list(s)
print(l)

from random import shuffle
l = [value for value in l if value == 'a']

print(l)

for item in enumerate('wordX'):
	print(item)

# com if SEM else

l = [(index, letter) for (index, letter) in enumerate('wordX') if index < len('wordX'[0:-1])]

print(l)

# com if else

l = [letter if index < len('wordX'[0:-1]) else 'Wont append the X' for (index, letter) in enumerate('wordX')]
print(l)

# nested loops

l = []

for x in [1, 2, 3]:
	for y in [1, 10, 100]:
		l.append(x*y)

print(l)

l = [x * y for x in [1, 2, 3] for y in [1, 10, 100]]
print('\nNow after listComprehension:\n', l)