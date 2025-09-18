class Computer:       
    #list of attributes of a computer and their types         
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    
    def __init__(self, description, processorType, hardDriveCapacity, memory, OS, year, price): 
        #setting up the computers
        self.description =  description
        self.processor_type = processorType
        self.hard_drive_capacity = hardDriveCapacity 
        self.memory = memory
        self.operating_system = OS
        self.year_made = year
        self.price = price

       
    def printComputerSetUp(self):
        #prints out all the components of the specific computer in a way that's easy to read
        #checks that the computer is set up correctly
        print ('Description:', self.description)
        print ('Processor Type:', self.processor_type)
        print ('Hard Drive Capacity:', self.hard_drive_capacity)
        print ('Memory:', self.memory)
        print ('Operating System:', self.operating_system)
        print ('Year Made:', self.year_made)
        print ('Price:', self.price)

    def refurbish(self):
        #update price based on age of machine

        print ("Refurbishing", self.description)

        if self.year_made < 2000:
            self.price = 0 # too old to sell, donation only
        elif self.year_made < 2012:
            self.price = 250 # heavily-discounted price on machines 10+ years old
        elif self.year_made < 2018:
            self.price = 550 # discounted price on machines 4-to-10 year old machines
        else:
            self.price = 1000 # recent stuff
    
        print ("New price is", self.price)
        print ("Done. \n")


    def updateOS(self, OS):
        #updates the operating system
        print ("Updating", self.description, "OS to", OS)
        print("Updating inventory...")
        self.operating_system = OS
        print("Done.\n")
     

def main():
    computer1: Computer = Computer('2018 MacBook Pro', 'Intel', 256, 16,'High Sierra', 2017, 1000)  
    

if __name__ == "__main__":
    main()