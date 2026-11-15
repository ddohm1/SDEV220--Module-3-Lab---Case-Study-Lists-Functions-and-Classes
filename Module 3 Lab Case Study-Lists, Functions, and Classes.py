#Dianna Dohm
#Module 3 Lab Case Study-Lists, Functions, and Classes.py
#App that outputs car data


class Vehicle():
    def __init__(self, vehicleType):
        self.vehicleType = vehicleType

class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
            self.year = year
            self.make = make
            self.model = model
            self.doors = doors
            self.roof = roof

print("Please input the information of your car when asked.")
while True:
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

while True:
    try:
        doorInput = int(input("How many doors does your car have? 2 or 4? "))
        if doorInput == 2 or doorInput == 4:
            break
        else:
            print("Please enter either 2 or 4.")
    except:
        print("Error: Please enter either 2 or 4.")

while True:
    roofInput = input("What kind of roof does your roof have? Solid or Sun Roof? ")
    roofInput = roofInput.title()
    if roofInput == "Solid" or roofInput == "Sun Roof":
        break
    else:
        print('Please type either "Solid" or "Sun Roof".')

car = Automobile(yearInput,makeInput, modelInput, doorInput, roofInput)

car.vehicleType = "Car"

print("\nHere is your vehicle!")
print("Vehicle Type: ", car.vehicleType)
print("Year: ", car.year)
print("Make: ", car.make.title())
print("Model: ", car.model.title())
print("Number of doors: ", car.doors)
print("Type of roof:  ", car.roof.title())