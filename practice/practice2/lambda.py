# square  = lambda x : x*x

people = [
	{"name" : "krishna", "book" : "geeta"},
	{"name" : "eckart", "book" : "power of now"},
	{"name" : "osho", "book" : "book of secrets"}
]

""" will cause error

people.sort()
print(people)
"""

 # key argument in sort may be used to specify which part of dictionary we to use to sort

"""
def f(person):
    return person["name"]
    
people.sort(key = f)
"""

people.sort(key = lambda person : person["name"])
print(people)