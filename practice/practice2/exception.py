# exception handling

import sys

try:
    x = int(input("x : "))
    y = int(input("y : "))  

# exception handler    
except ValueError:
    print("invalid input: cannot enter string for division")
    
    """ exit the pprogram with status code of 1, 
    where status code of 1 means something went wrong in this program
    """
    sys.exit(1)
    
try:
    result = x/y
except ZeroDivisionError:
    # string cannot be converted into base 10 integer
    print("invald input: cannot divide by zero")     
    sys.exit(1)

print(f"{x}/{y} = {result}")	

"""
    ZeroDivisionError: division by zero
    ValueError: invalid literal for int() with base 10: 'sdg'
"""