def hi():
    """ this is also fine
    return print('hi')
    """
    print('hi')

def loop(f, n):  # f repeats n times
    if n <= 0:
        return
    else:
        f()
        loop(f, n-1)
 
""" TypeError: 'NoneType' object is not callable 
loop(hi(),3)
"""

loop(hi,3)