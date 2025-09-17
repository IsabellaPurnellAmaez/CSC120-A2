from computer import Computer

class ResaleShop:

    # What attributes will it need?

    inventory = []

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory:list):
        self.inventory = inventory 
    # What methods will you need?

    

    def buy(self, computer:Computer):
        self.inventory.append(computer)
        #1. call Computer(...) constructor #to create a new computer instance <== ASK ABOUT THIS STEP IN TUTORING!!
        #2. call inventory.append(...) to add the new computer to the inventory


    def sell(self, computer:Computer):
        self.inventory.remove(computer)

    def print_inventory(self):
        print(self.inventory)


def main():
    computer1: Computer = Computer('2018 MacBook Pro', 'Intel', 256, 16,'High Sierra', 2017, 1000)  
if __name__ == "__main__":
    main()