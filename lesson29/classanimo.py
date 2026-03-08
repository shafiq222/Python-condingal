from abc import ABC, abstractmethod

class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk")

class Snake(Animal):
    def move(self):
        print("I can glid")

class Dog(Animal):
    def move(self):
        print("I can bark")

class Lion(Animal):
    def move(self):
        print("I can roar")
R = Human()
R.move()

K = Snake()
K.move()

A = Dog()
A.move()

B = Lion()
B.move()







