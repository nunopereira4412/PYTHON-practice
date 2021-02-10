class Animal():

	def __init__(self):
		self.type = 'animal'
		self.legs = 'depends'
		print('Animal created')

	def eat(self):
		print('eating...')

	def whoAmI(self):
		print('I am an animal')

	def __str__(self):
		return f'My type is {self.type} and i have {self.legs} legs'

	def __del__(self):
		print('An animal has been deleted')


class Dog(Animal):

	def __init__(self):
		Animal.__init__(self)
		self.type = 'dog'
		self.legs = 4
		print('Dog created')

	def whoAmI(self):
		print('I am a dog')

	def bark(self):
		print('WHOF WHOF')

	def __str__(self):
		return f'My type is {self.type} and i have {self.legs} legs'

	def __del__(self):
		print('A dog has been deleted')


animal = Animal()
dog = Dog()

animal.eat()
animal.whoAmI()

dog.eat()
dog.whoAmI()
dog.bark()

for petClass in [animal, dog]:
	print(type(petClass))
	print(type(petClass.whoAmI()))

print(animal)
print(dog)
del(dog)


