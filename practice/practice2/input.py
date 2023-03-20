name = input("Name : ")
print("Hello " + name )

# to import square function from functions.py module
from functions import square

# to import entire functions.py module
import functions
 
print(f"Hello {name}")

# if we use double quotes within double quotes, it will cause error

print(f"Hello {input('Name: ')}")

names = ["vibhav", "ankur"]
# create an empty set
s = set()
# create an empty dictionary
houses = {}

n = int(input("Number : "))
if n > 0:
    print("number is positive")
    for i in range(n) :
        names.append(input("enter name : "))
        s.add(int(input("value to add : ")))
        
    print(names)
    s.remove(int(input("value to remove : ")))
    print(s)
    print(f"set has length {len(s)}")
    
elif n < 0:
    print("number is negative")
else:
    print("number is zero")

if n >= 0 :   
    for i in range(n + 2) :
        print(f"first character of {names[i]} is {names[i][0]}")    
        houses[names[i]] = input("enter value for the key " + names[i] + " : ") 
        print(houses[names[i]])
    
for name in names:
    print(name)
for character in names[n + 1]:
    print(character)
    
for i in range(10) :
    print(f"the square of {i} is {square(i)}")
    
    print(f"the square of {i} is {functions.square(i)}")
        

        
    