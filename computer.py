class Computer:

    # What attributes will it need?
    
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description, processorType, hardDriveCapacity, memory, OS, year, price):
        self.description =  description
        self.processor_type = processorType
        self.hard_drive_capacity = hardDriveCapacity 
        self.memory = memory
        self.operating_system = OS
        self.year_made = year
        self.price = price

       
        
    # What methods will you need?
    def printComputerSetUp(self):
        print ({'description': self.description, 'processor_type': self.processor_type, 'hard_drive_capacity': self.hard_drive_capacity, 'memory': self.memory, 'operating_system': self.operating_system, 'year_made': self.year_made, 'price':self.price})
    
    def refurbish(self, OS:str):
        self.operating_system = OS

def main():
    computer1: Computer = Computer('2018 MacBook Pro', 'Intel', 256, 16,'High Sierra', 2019, 1000)
    computer1.printComputerSetUp()
    computer1.refurbish("ah")
    computer1.printComputerSetUp()

if __name__ == "__main__":
    main()