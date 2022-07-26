# Exercise with Inheritance 
# Create Panda class that inherits form the Mammal class. Make Panda inherit from the Mammal class. 
# Make Panda have attribute is_endangered=True and code as instance attrride of code. 
class Mammal:
    def __init__(self, name, age, health, num_offspring, years_in_captivity):
        self.name = name
        self.age = age
        self.health = health
        self.num_offspring = num_offspring
        self.years_in_captivity = years_in_captivity

# Define the Panda class below this line
class Panada(Mammal):
    def __init__(self, name, age, health, num_offspring,years_in_captivity, code):
        is_endangered = True
        Mammal.__init__(self, name, age, health, num_offspring,years_in_captivity)
        self.code = code

my_panda = Panada("Travis", 2 , "Okay", 0, 2, 33212)