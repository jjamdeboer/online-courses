# METHODS ARE BUILT-IN FUNCTIONS

DURK = 'HELLO'

def name_of_function(DURK):
    """
    DOCSTRING EXPLANATION
    """
    return (DURK + ' DUUUUUUUUUUUUUUUUUUUURK')

print(name_of_function(DURK))
# help(name_of_function)

# TO PUT IN DEFAULT VALUE
def name_of_function2(DURK = 'DUUUUUUUURK'):
    """
    DOCSTRING EXPLANATION
    """
    return (DURK + ' DUUUUUUUUUUUUUUUUUUUURK')

print(name_of_function2())

# ARGUMENTS AND KEYWORD ARGUMENTS *args **kwargs

def function(*args):
    return sum(args)/3 +19

# ARGS RETURNS TUPLE
print(function(3,6,2,31,3,24,34,512,321,5,25,5,3,))

# KWARGS RETURNS DINCTIONAIRIES
def function2(**kwargs):
    return "HELLO" in kwargs.values()

print(function2(gh = "fruit", hi = "HELLO"))