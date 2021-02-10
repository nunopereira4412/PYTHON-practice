def kargsTest(**kargs):
	print(kargs)
	if 'fruit' in kargs:
		print(kargs['fruit'])
	print('Didnt find my fruit')

kargsTest(frut='sdfsdf', fruit='apple', rrrr='rrrr')
