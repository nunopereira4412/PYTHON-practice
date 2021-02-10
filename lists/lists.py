l = [1, 'asdasd', 11.22, 4, 5, 6, 'qqqq']

anotherl = [11111111111, 222222222]

# slicing and indexing

print(l[1:])

print(l + anotherl)

#adds an element to the end of the lpytj

l.append('APPENDED')

print(l)

# removes last element from l

popped = l.pop(-1) # OR popped = l.pop()

print(l)

print(popped)

popped = l.pop(0)

print(l)

# sorting

l = [5, 3, 2, 5, 7, 10]
print(l)

# ERRO l = [1, 'ee', 'fffff', 4]

l.sort()

sortedL = l
print(sortedL)

# NoneType
print(type(sortedL))

sortedL.append(sortedL.pop())

print(sortedL)

sortedL.pop()

print(sortedL)



