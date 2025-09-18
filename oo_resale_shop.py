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
        print("Buying", computer.description)
        print("Adding to inventory...")
        self.inventory.append(computer)
        print("Done.\n")

       

    def sell(self, computer:Computer):
        self.inventory.remove(computer)

    def print_inventory(self):
        for i in range (len(self.inventory)):
            print ('Description:', self.inventory[i].description)
            print ('Processor Type:', self.inventory[i].processor_type)
            print ('Hard Drive Capacity:', self.inventory[i].hard_drive_capacity)
            print ('Memory:', self.inventory[i].memory)
            print ('Operating System:', self.inventory[i].operating_system)
            print ('Year Made:', self.inventory[i].year_made)
            print ('Price:', self.inventory[i].price)
            print ('\n')



def main():
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21, '\n')
    
    Resale_Shop: ResaleShop = ResaleShop([])
    
    computer1: Computer = Computer('2018 MacBook Pro', 'Intel', 256, 16,'High Sierra', 2017, 1000)  
    computer2: Computer = Computer('Mac Pro (Late 2013)', '3.5 GHc 6-Core Intel Xeon E5', 1024, 64, 'MacOS Monterey', 2013, 550)  

    Resale_Shop.buy(computer1)
    Resale_Shop.buy(computer2)

    Resale_Shop.print_inventory()

    computer1.refurbish()

    computer2.updateOS('High Sierra')

    Resale_Shop.sell(computer1)

    Resale_Shop.print_inventory()


    
if __name__ == "__main__":
    main()