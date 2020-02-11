# Imports
import keyboard
from time import sleep
# Variables
commands = "o: +1 commercial office\nt: +1 tree\nh: +1 average house\np: Calculate emissions\nShift: Go 10x faster when adding trees, buildings, etc.\nCtrl: Add 10 trees, buildings, etc. at a time"
# Functions / Classes
class co2Object:
    def __init__(self, co2, amount):
        self.co2 = co2
        self.amount = amount
    def increase(self):
        self.amount += 1
    def decrease(self):
        self.amount -= 1
def delaywithShift():
    if keyboard.is_pressed("shift"):
        sleep(0.01)
    else:
        sleep(0.1)
def fancySplit():
    print("===============================================================")
# Code
office = co2Object(125, 0)
tree = co2Object(-0.025, 0)
house = co2Object(48, 0)
print("Press the corresponding buttons on your computer to run the commands:")
print(commands)
while True:
    if keyboard.is_pressed("o"):
        if keyboard.is_pressed("ctrl"):
            print("+10 commercial office")
            for i in range(10):
                office.increase()
        else:
            print("+1 commercial office")
            office.increase()
        delaywithShift()
    if keyboard.is_pressed("t"):
        if keyboard.is_pressed("ctrl"):
            print("+10 trees")
            for i in range(10):
                tree.increase()
        else:
            print("+1 tree")
            tree.increase()
        delaywithShift()
    if keyboard.is_pressed("h"):
        if keyboard.is_pressed("ctrl"):
            print("+10 average houses")
            for i in range(10):
                house.increase()
        else:
            print("+1 house")
            house.increase()
        delaywithShift()
    if keyboard.is_pressed("p"):
        fancySplit()
        print("")
        print("Calculating carbon emissions...")
        sleep(1)
        print(str((office.amount * office.co2) + (tree.amount * tree.co2) + (house.amount * house.co2)) + " tons/year")
        print("")
        print("Amount of each:")
        print(str(office.amount) + " commercial office(s)")
        print(str(tree.amount) + " tree(s)")
        print(str(house.amount) + " house(s)")
        print("")
        print("Cost of trees:")
        print("Buying trees: $" + str(tree.amount * 0.3))
        print("Planting trees: $" + str(tree.amount * 1) + "-" + str(tree.amount * 10))
        print("Total cost: $" + str((tree.amount * 0.3) + (tree.amount * 1)) + "-" + str((tree.amount * 0.3) + (tree.amount * 10)))
        print("")
        print("Amount of space taken up:")
        print("Office(s): " + str(office.amount * 10000) + " sq. ft.")
        print("Tree(s): " + str(tree.amount * 25) + " sq. ft.")
        print("House(s): " + str(house.amount * 2000) + " sq. ft.")
        print("")
        fancySplit()
