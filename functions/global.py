x = 0

print(x)

def func():
	#try comment to 
	global x

	print(x)

	x = 200
	print(x)

func()

print(x)