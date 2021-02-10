# 'String here {} then also {}'.format('something1', 'something2')

teste = 'TESTE'

x = 'X' 

s = 'um {} dois tres {}'.format(teste, x)

print(s)

# podemos usar o index dentro do format e meter dentro das {}

s = 'um {1} tres {0} cinco'.format('quatro', 'dois')

print(s)

# agora com keywords, é possivle ter mais opçoes de formatting que {}'s

s = 'um {d} tres {q} cinco'.format(q = 'quatro', d = 'dois', a='asd')

print(s)

# another way

name = 'TESTE'
age = 3

print(f'Isto é um {name}')
print(f'Name = {name} with {age} years old')


