f = open("populateCamara.txt", "w")

numCamara = 0

while numCamara < 10001:
	f.write(f'insert into Camara values (\'{numCamara}\');\n')
	numCamara += 1