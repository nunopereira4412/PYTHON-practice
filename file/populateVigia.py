f = open("populateVigia.sql", "w")

numCamara = 0


while numCamara < 10001:
	f.write(f'insert into vigia values (\'local_{numCamara}\', \'{numCamara}\');\n')
	numCamara += 1