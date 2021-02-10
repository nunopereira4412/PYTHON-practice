l = [1, 2, 3, 4, 5]

mySum = 0

print(type(l))

for a in l:
	if a % 2:  
		print(a)
		mySum += a
	else:
		print(f'Odd number {a}')

print(f'mySum: {mySum}')

s = 'my string'

for letter in s:
	print(letter)
	print(letter.upper())

#or

# for letter in 'my string':
# 	print(letter)
# 	print(letter.upper())

for _ in 'something':
	print('cool')

d = {'dez':10, 'vinte':20, 'trinta':'TRIIIINTA'}

l2 = [(0, 1, 2), (1, 2, 3), (2, 3, 4)]

for (a, b, c) in l2:
	print(b)

for item in d:
	print(item, ':', d[item])

for item in d.items():
	print(item)

for key in d.keys():
	print(key)

for value in d.values():
	print(value)

