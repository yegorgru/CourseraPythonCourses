class Animal:
	name = 'Abstract'

	def __init__(self, name):
		self.name = name
		print('based', self.name)

	def makeSound(self):
		print('abstract sound')

	def __del__(self):
		print('By from base')

class Cat(Animal):
	def __init__(self, name):
		#Animal.__init__(self, name)
		super().__init__(name)
		print('Hi, I am cat', self.name)

	def makeSound(self):
		print('Meoww')

	def __del__(self):
		#Animal.__del__(self)
		super().__del__()
		print('By from cat')

m = Cat('Bagira')
m.makeSound()
