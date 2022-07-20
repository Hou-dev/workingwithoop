#simple class, inheritance and polymorphism examples in python.
class Animal:
    def __init__(self,name,age,height,weight):
        self.age = age
        self.height = height
        self.weight = weight
        self.name = name
    
    def display(self):
        return f"Hi this is {self.name}, they are {self.age} year(s) old and weight {self.weight} kg and {self.height} cm tall"

class Bird(Animal):
    def communicate(self):
        return 'Squawk'
    
class Dog(Animal):
    def communicate(self):
        return 'Woof'
    

parrot = Bird("Root", 1, 20, 2)
print(parrot.communicate())