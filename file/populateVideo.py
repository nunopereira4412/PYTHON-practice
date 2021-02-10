f = open("populateVideo.sql", "w")

numCamara = 0


while numCamara < 10001:
	f.write(f'insert into video values (\'2018-01-01 00:00:00\', \'2018-01-01 01:00:00\', \'{numCamara}\');\n')
	numCamara += 1