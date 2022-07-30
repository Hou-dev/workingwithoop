# Inhieritance pactice
# Define ScienceProfessor which is a subclass of Professor
# add greet_students in method SciencProfesor and print line
# call greet_students from Professor superclass

class Professor:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        
    def greet_students(self):
        print("Welcome to class!")

# Define your class below this line
class ScienceProfessor(Professor):
    def __init__(self, name, age, course):
        Professor.__init__(self, name, age, course)
    
    def greet_students(self):
        print("Hi everyone! It's a great day to study Science!")
        Professor.greet_students(self)

science_professor = ScienceProfessor("James", 28, "Software Engineering")



# Create DonutStore subclass
class Store:
    def __init__(self, name, address, num_employees):
        self.name = name
        self.address = address
        self.num_employees = num_employees
        
    def greet_customers(self):
        print("Welcome to our store! What would you like to buy?")
        
# Create your DonutStore class below this line

class DonutStore(Store):
    def __init__(self, name, address, num_employees):
        super().__init__(name, address, num_employees)
    def greet_customers(self):
        print("Welcome to our store! What donut would you like to eat?")


my_donut_store = DonutStore("James", "London, England", 10)
