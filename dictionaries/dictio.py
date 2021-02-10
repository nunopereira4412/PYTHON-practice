l = [12, 'asasd', 12]

d = {'dez':10, 'vinte':20, 'trinta':'TRIIIINTA'}

dictio = {'a':'aaaaa', 'b':'BBBbbbBB', 'dois':2, 'lista':l, 'dic':d}

print(type(l))
print(type(d))
print(type(dictio))

print(dictio['b'])
print(dictio['dois'])

print(dictio['lista'][1])
print(dictio['lista'][2])

print(dictio['dic'])

print(dictio['dic']['dez'])
print(dictio['dic']['trinta'].lower())

print(dictio['dic']['trinta'][-1].lower())

# add new element to dictionary

dictio['C'] = 'CCCCCCccCCC'

print(dictio['C'])

#override existing element 'a'

print(dictio)

dictio['a'] = 'NEW AAAA'

print(dictio['a'])

# get all keys from a dict

print(dictio.keys())
print('\n\n')
print(dictio.values())
print('\n\n')
print(dictio.items())