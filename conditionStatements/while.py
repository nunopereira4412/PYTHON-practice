x = 0

while x < 5:
	if x == 3 or x == 4:
		x += 1
		continue
		pass
	print(f'current x value is: {x}')
	x += 1
else: 
	print('x is now >= 5')