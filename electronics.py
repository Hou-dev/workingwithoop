# Welcome to this assignment!
# For this assignment, you are free to design your classes as you wish. Include attributes and methods.
# Follow the diagram below to create your classes and represent this hierarchy.
# Submit your code for the assignment.

class ElectronicDevice:
    def __init__(self,resistance, capacitance, inductance):
        self.resistance = resistance
        self.capacitance = capacitance
        self.inductance = inductance

class Computer(ElectronicDevice):
    def __init__(self, resistance, capacitance, inductance, dpi, size, color):
        ElectronicDevice.__init__(self, resistance, capacitance, inductance)
        self.dpi = dpi
        self.size = size
        self.color = color

class TV(ElectronicDevice):
    def __init__(self, resistance, capacitance, inductance,dpi,size,color,age):
        ElectronicDevice.__init__(self, resistance, capacitance, inductance)
        self.dpi = dpi
        self.size = size
        self.color = color
        self.age = age

class Desktop(Computer):
    def __init__(self, resistance, capacitance, inductance, dpi, size, color, style):
        Computer.__init__(self, resistance, capacitance, inductance, dpi, size, color)
        self.style = style

class Laptop(Computer):
    def __init__(self, resistance, capacitance, inductance, dpi, size, color, battery):
        Computer.__init__(self, resistance, capacitance, inductance, dpi, size, color)
        self.battery = battery
        
my_laptop = Laptop(80, 20, 11, 280, 17, "DCI-P3", "20 kWH")
print(my_laptop.battery)