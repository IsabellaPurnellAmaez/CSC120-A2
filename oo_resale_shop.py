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
        self.inventory.append(Computer)
        #1. call Computer(...) constructor #to create a new computer instance
        #2. call inventory.append(...) to add the new computer to the inventory

    def update_price(self):
        pass

    def sell(self):
        pass

    def print_inventory(self):
        pass


def main():
   computer1: Computer = Computer()

if __name__ == "__main__":
    main()