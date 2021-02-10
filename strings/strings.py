print("hello world")

x = 2

# tipo da variavel

print(type(x))

print(x**10)

x = "im a string" + "TETETET"

print(x[0])

# ultimo elemento da string
print(x[-1])

print(type(x))

x = 2.2

y = 4


print(type(x))

x = ["Sammy", 'testeeeeee', 2]

print(x[2]+y)

print(type(x))

x = 'aaabbbcccdd'

y = 'aaa\nbbcccd'

print(x[0 : -1 : 3])

print(y[0 : -1 : 3])

#lenght

z = len(x)
print(z)

# slicing de strings

print(x[3:])
print(x[:3])
print(x[::3])
print(x[3:6])
print(x[::])

# print reverse

print(x[::-1])

# mudar o 'S' para 'P'
name = "Sam"

print(name)

lastLetters = name[1:]

print('P' + lastLetters)

# having one 'z' get 10 'z'

name = 'z'

print(name)
print(name * 10)

# upper case

name = 'um'

print(name)
print(name.upper())

# split and print 1 of the resulting strings
name = name + ' dois'
splittedString = name.split()

print(splittedString[1] + ' ' + splittedString[0])

# splitString on what we want

splittedOnI = name.split('i')
print(splittedOnI)

name = "teste '' a"
print(name)

name = name.split('e');

print(name);

name = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(len(name))
print(name[0:10])

#print reserve starting on -1 = 9 and until -5 = 5
print(name[-1:-5:-1])









