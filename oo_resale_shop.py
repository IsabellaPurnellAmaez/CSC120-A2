from computer import Computer

class ResaleShop:

    inventory = [] #the only thing the ResaleShop needs is an inventory to be modified

    def __init__(self, inventory:list):
        self.inventory = inventory          #defines the inventory


    def buy(self, computer:Computer):       #to buy a computer/add computer to inventory
        print("Buying", computer.description)
        print("Adding to inventory...")
        self.inventory.append(computer)
        print("Done.\n")

       

    def sell(self, computer:Computer):      #to sell a computer/remove from inventory
        self.inventory.remove(computer)
        if computer not in self.inventory:
            print("Sorry, that computer isn't in our inventory")        #error message incase someone tries to remove a computer that doesn't exist

    def print_inventory(self):              #to neatly print inventory so it can be viewed in the terminal
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
    print("-" * 21)                 #nice banner 
    print("COMPUTER RESALE STORE")
    print("-" * 21, '\n')           
    
    Resale_Shop: ResaleShop = ResaleShop([])    #setting up our resale shop
    
    #make computers
    computer1: Computer = Computer('2018 MacBook Pro', 'Intel', 256, 16,'High Sierra', 2017, 1000)  
    computer2: Computer = Computer('Mac Pro (Late 2013)', '3.5 GHc 6-Core Intel Xeon E5', 1024, 64, 'MacOS Monterey', 2013, 550)  

    #resale shop buys computers
    Resale_Shop.buy(computer1)
    Resale_Shop.buy(computer2)

    #tests to ensure the program works
    Resale_Shop.print_inventory()

    computer1.refurbish()

    computer2.updateOS('High Sierra')

    Resale_Shop.sell(computer1)

    Resale_Shop.print_inventory()


    
if __name__ == "__main__":
    main()