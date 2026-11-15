#Dianna Dohm
#Module 3 Lab Case Study-Lists, Functions, and Classes.py
#App that outputs car data

#yearInput is an integer holding input from the user about the car's year
#makeInput is a string holding input from the user about the car's make
#modelInput is a string holding input from the user about the car's model
#doorInput is an integer holding input from the user about the amount of doors the car has
#roofInput is a string holding input from the user about the car's roof type

#parent class
class Vehicle():
    def __init__(self, vehicleType):
        self.vehicleType = vehicleType

#child class
class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
            self.year = year
            self.make = make
            self.model = model
            self.doors = doors
            self.roof = roof

print("Please input the information of your car when asked.")#intro
while True:#input validation for the year
    try:
        yearInput = int(input("What is the year of your car? "))
        if yearInput > 1884 and yearInput < 2028:
            break
        else:
            print("Please enter a year between 1885 and 2027.")
    except:
        print("Error: Please enter a year between 1885 and 2027.")
         

makeInput = input("What is the make of your car? ")
modelInput = input("What is the model of your car? ")

while True:#input validation for the amount of doors
    try:
        doorInput = int(input("How many doors does your car have? 2 or 4? "))
        if doorInput == 2 or doorInput == 4:
            break
        else:
            print("Please enter either 2 or 4.")
    except:
        print("Error: Please enter either 2 or 4.")

while True:#input validation for the type of roof
    roofInput = input("What kind of roof does your roof have? Solid or Sun Roof? ")
    roofInput = roofInput.title()
    if roofInput == "Solid" or roofInput == "Sun Roof":
        break
    else:
        print('Please type either "Solid" or "Sun Roof".')

#makes the car object
car = Automobile(yearInput,makeInput, modelInput, doorInput, roofInput)

car.vehicleType = "Car"

#prints output
print("\nHere is your vehicle!")
print("Vehicle Type: ", car.vehicleType)
print("Year: ", car.year)
print("Make: ", car.make.title())
print("Model: ", car.model.title())
print("Number of doors: ", car.doors)
print("Type of roof:  ", car.roof.title())