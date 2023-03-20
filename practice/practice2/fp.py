""" Functional programming paradigm : functions are like values in python
unlike other programming languages, in python a function is like a value. We can pass it like an
input to another function and get it as the output of another function
Decorator is a function that take a function as input, modifies, add an additional behaviour to that 
function and returns modified version of that function as ouptut

"""

""" This is also working
def announce(f):
    def wrapper():
        print("About to run the function")
        f()
        print("Done with the function")
    
    return wrapper()


def hello():
    print("Hello vibhav")
    
announce(hello)          
"""

# we can also do in following way using decorator. here lines 25 to 35 is decorator

def announce(f):

    """  announce decorator modifies f by creating a new function which wraps up f with some additional 
    behaviour
    """
    
    def wrapper():
        print("About to run the function")
        f()
        print("Done with the function")
    
    """ Absence of 'return wrapper' will cause TypeError: 'NoneType' object is not callable
    'return wrapper' returns wrapper function. 'return wrapper()' will also cause same error
    """
    # announce decorator returns a new function
    return wrapper

""" to add decorator we use @. to add announce decorator to function hello. Now hello function is wrapped
inside of this announce decorator
Decorators are helpful in web applications where we want to run certain functions after checking if the user is logged in

"""
   
@announce
def hello():
    print("Hello vibhav")
    
hello()