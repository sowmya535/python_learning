# #single inheritance
# class Animal:
#     def eat(self):
#         print("Animal is eating")
# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")
# d = Dog()
# d.eat()
# d.bark()


# #multiple inheritance
# class Animal:
#     def eat(self):
#         print("Animal is eating")
# class Dog:
#     def bark(self):
#         print("Dog is barking")
# class puppy(Animal, Dog):
#     def play(self):
#         print("puppy is playing")
# d = puppy()
# d.eat()
# d.bark()
# d.play()


# #hierarchal inheritance
# class Animal:
#     def eat(self):
#         print("Animal is eating")
# class Dog(Animal):
#     def bark(self):
#         print("dog is barking")
# class Cat(Animal):
#     def meow(self):
#         print("cat is meowing")
# d = Dog()
# c = Cat()

# d.eat()
# d.bark()

# c.eat()
# c.meow()


# #multilevel inheriance
# class Animal:
#     def eat(self):
#         print("Animal is eating")
# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")
# class puppy(Dog):
#     def play(self):
#         print("Puppy is playing")
# p = puppy()
# p.eat()
# p.bark()
# p.play()


#hybrid inheritance
class Animal:
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
class Cat(Animal):
    def meow(self):
        print("Cat is meowing")
class Puppy(Dog, Cat):
    def play(self):
        print("Puppy is playing")
p = Puppy()
p.eat()
p.bark()
p.meow()
p.play()     


