class myClass():

	# class object attributes
	# will always remain the same
	wontChange = 'neverChange'

	def __init__(self, a = 0, b = 0): #default values to 0
		self.a = a
		self.b = b
		self.c = 100

	def printParams(self):
		print(self.a)
		print(self.b)
		print(self.c)
		print(myClass.wontChange)
		print(f'TEST a = {self.a}, b = {self.b}, cObjectAttr = {myClass.wontChange}')

	def testPrintOutside(self, outside):
		print(outside)

a = myClass(a = 1, b = 'afffsdf')
b = myClass()

print(a.a, a.b)

print(a.wontChange)

a.printParams()
b.printParams()

a.testPrintOutside(3)

