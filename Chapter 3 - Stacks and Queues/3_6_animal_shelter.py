class Animal(object):
	def __init__(self, animalName=None, animalType=None, next=None):
		self.animalName = animalName
		self.animalType = animalType
		self.next = next
		self.timestamp = 0 # to keep track of the order of arrival of the animals

class AnimalShelter(object):
	def __init__(self):
		self.headCat = None
		self.tailCat = None
		self.headDog = None
		self.tailDog = None
		self.animalNumber = 0

	def enqueue(self, animalName, animalType):
		self.animalNumber += 1 
		newAnimal = Animal(animalName, animalType)
		newAnimal.timestamp = self.animalNumber

		if animalType == 'cat':
			if not self.headCat:
				self.headCat = newAnimal
			if self.tailCat:
				self.tailCat.next = newAnimal
			self.tailCat = newAnimal

		elif animalType == 'dog':
			if not self.headDog:
				self.headDog = newAnimal
			if self.tailDog:
				self.tailDog.next = newAnimal
			self.tailDog = newAnimal

	def dequeueCat(self):
		if self.headCat:
			newAnimal = self.headCat
			self.headCat = newAnimal.next
			return str(newAnimal.animalName)
		else:
			return "No cat left!"

	def dequeueDog(self):
		if self.headDog:
			newAnimal = self.headDog
			self.headDog = newAnimal.next
			return str(newAnimal.animalName)
		else:
			return "No dog left!"

	def dequeueAny(self):
		if self.headCat and not self.headDog:
			return self.dequeueCat()
		elif not self.headCat and self.headDog:
			return self.dequeueDog()
		elif self.headCat:
			if self.headCat.timestamp < self.headDog.timestamp:
				return self.dequeueCat()
			else:
				return self.dequeueDog()
		else:
			return "No animal left!"

	def display(self):
		print('The list of cats : ')
		cats = self.headCat
		countCat = 1
		while cats != None:
			print("#{} : {}.".format(countCat,cats.animalName))
			cats = cats.next
			countCat += 1

		print('\nThe list of dogs : ')
		dogs = self.headDog
		countDog = 1
		while dogs:
			print("#{} : {}.".format(countDog,dogs.animalName))
			dogs = dogs.next
			countDog += 1

if __name__ == "__main__":
	AS = AnimalShelter()
	AS.enqueue('mia', 'cat')
	AS.enqueue('tommy', 'dog')
	AS.enqueue('lisa', 'cat')
	AS.enqueue('bruno', 'dog')
	AS.enqueue('brando', 'dog')
	AS.enqueue('molly', 'cat')
	AS.display()

	print("\nSelect a cat")
	print(AS.dequeueCat())
	print("\nSelect a dog")
	print(AS.dequeueDog())
	print("\nSelect any animal")
	print(AS.dequeueAny())
