class Animal:
    def make_sound(self):
        print("Some sound")
class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")
animal = Animal()
dog = Dog()
cat = Cat()
animal.make_sound()
dog.make_sound()
cat.make_sound()
