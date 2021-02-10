f = open("populateLocal.sql", "w")

numCamara = 0


while numCamara < 10001:
	f.write(f'insert into local values (\'local_{numCamara}\');\n')
	numCamara += 1