""" oop is programming that is centered around objects to store information and perform funtions
class is template for a new type of object
keyword self is representing object we are currently working with, it should be the first argument 
for any method within a class
"""
class point():
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
p = point(2,8)
print(p.x)
print(p.y)
# object Oriented programming

class flight():
    # method to create new flight with given capacity
    def __init__(self, capacity) :
        self.capacity = capacity
        self.passengers = []

    # method to add passenger to flight
    def add_passenger(self, name) :
        if not self.open_seats() :
            return False

        self.passengers.append(name)
        return True
        
    def open_seats(self) :
        return self.capacity - len(self.passengers)
        
# create a new flight with capacity of 3 passengers

flight = flight(int(input("enter capacity : ")))

# create a list of passengers
people = ["vibhav", "krishna", "osho", "eckart"]

# what if i want to accept people as input ?

# attempt to add each person in list to flight

for person in people :
    if flight.add_passenger(person) : 
        print(f"passenger {person} added successfully")
    else :
        print(f"no seat available for {person}")
    