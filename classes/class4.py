class Animal:
    def __init__(self, name):
        self.name = name
    def sit(self):
        print(self.name + " is sitting.")
    def eat(self):
        print(self.name + " is eating.")
    def sleep(self):
        print(self.name + " is sleeping.")
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def bark(self):
        print(self.name + " is barking.")
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    def meow(self):
        print(self.name + " is meowing.")
my_dog = Dog('JONI', 'GUCHI')
print(my_dog.name + " is a great dog!")
my_dog.sit()
my_dog.eat()
my_dog.sleep()
my_dog.bark()
my_cat = Cat('Daisy', 'Mano')
print(my_cat.name + " is a lovely cat!")
my_cat.sit()
my_cat.eat()
my_cat.sleep()
my_cat.meow()