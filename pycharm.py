class Flight():
    def __init__(self, capacity, name):
        self.capacity = capacity
        self.name = name
        
    def Pname(self):
        print(f"the name of the first passenger is {self.name}")
        
flight = Flight(2, "fidelis")
flight.Pname()
