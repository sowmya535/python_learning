# from abc import ABC, abstractmethod
# class Car(ABC):
#     @abstractmethod
#     def start(self):
#         pass
# class BMW(Car):
#     def start(self):
#         print("Car starts with a button")
# c = BMW()
# c.start()


from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass
class Dog(Animal):
    def eat(self):
        print("Dog is eating")
d = Dog()
d.eat()