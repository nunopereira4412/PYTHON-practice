import itertools

# n = int(input('Enter children number:'))
# sShapes = input('Enter shapes:')
# sPrefs = input('Enter prefs:')

# sShapes = sShapes.split(' ')
# sPrefs = sPrefs.split(' ')

# shapes = []
# prefs = []

# for shape in sShapes:
# 	shapes.append(int(shape))

# for pref in sPrefs:
# 	prefs.append(int(pref))

# print(shapes)
# print(prefs)

# index = 0

# def checkEnd(shapes, prefs):
# 	return (shapes[index] == 1 and sum(prefs) == 0) or (shapes[index] == 0 and sum(prefs) == len(prefs))

# while not(checkEnd(shapes, prefs)):	
# 	if shapes[0] == prefs[index]:
# 		shapes.pop(0)
# 		prefs.pop(0)
# 	else:
# 		prefs.append(prefs[index])
# 		prefs.pop(0)
	
# 	if index < n - 1:
# 		index += 1
# 	else:
# 		index = 0 

# 	print(shapes)
# 	print(prefs)
# 	print(index)


# print(len(prefs))

# list = [1, 2, 3]

# print(list)
# print(list[-1:-1])

################################
################################

# x = 1

# a = [0, 1, 2]

# a.insert(0, a[x])
# a.pop(x+1)

# a = (1, 1, 1)
# a[0] = 2

# print(a)

################################
################################

lst = list(itertools.product([0, 1], repeat=3))
print(lst)

a = (5, 5, 5)

print(len(a))

lst.append(a)

print(lst)

c = [0, 0]

b = list(c)

print(c)
print(b)










