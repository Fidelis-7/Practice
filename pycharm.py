class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passenger = []

    
    def add_passenger(self, name):
        if self.open_seats():
            self.passenger.append(name)
            return True
        else:
            print("pls all seats are taken")
            return False
        
        
    def open_seats(self):
        return self.capacity - len(self.passenger)
        
flight = Flight(3)
people = ["fidelis", "obed", "nams", "Debbie"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"congrats {person} added")
    else:
        print(f"space is full {person}")