# Your job is to add three methods to the existing program:

# 1. A method print_students_data that prints the name of each one of the students in the dictionary, their age, and the classes they are taking, one student per line.

# A sample output would be:

# "Student: Gino who is 15 years old and is taking ['Piano', 'Guitar']"
# "Student: Talina who is 28 years old and is taking ['Cello']"
# "Student: Eric who is 12 years old and is taking ['Singing']"
# 2. A method print_student that prints the string shown above with the name, age, and classes of a student. It should take the name of the student as an argument and print only the data of that particular student. (Tip: you might consider using this method in the print_students_data  method to avoid repetition).

# 3. A method add_student  that adds a student to the existing students dictionary. The key used to add the student to the dictionary should be the name of the student and the value should be a list with the age, phone number, and classes that the student is taking. The method should take the name of the student as a parameter and a list with the data associated with that name as another parameter.



class MusicSchool:
    students = {"Gino":   [15, "653-235-345", ["Piano", "Guitar"]],
		    "Talina": [28, "555-765-452", ["Cello"]],
		    "Eric":   [12, "583-356-223", ["Singing"]]}
    def __init__(self, working_hours, revenue):
        self.working_hours = working_hours
        self.revenue = revenue
	# Add your methods below this line
    def print_students_data(self):
        for items in MusicSchool.students:
            self.print_student(items)
    
    
    # Create the instance
    def print_student(self,name):
        data = MusicSchool.students[name]
        print("Student: " + name + " who is " + str(data[0]) + " years old and is taking " + str(data[2]))
    
    def add_student(self, name , data):
        MusicSchool.students[name] = data
 
# Call the methods
testClass = MusicSchool(10,20000)
testClass.add_student("Mark", [20, "888-111-8734", ["Drums"]])
testClass.print_students_data()