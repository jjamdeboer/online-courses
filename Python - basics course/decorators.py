# DECORATOR: ON/OFF SWITCH FOR EXTRA FUNCTIONALITY IN YOUR FUNCTIONS, DENOTED BY @

# @some_decorator
# def some_function:
#     do stuff
#     return something

# FUNCTIONS ARE OBJECTS THAT CAN BE PASSED INTO OTHER OBJECTS:

def some_function():
    return "DUUUUUUUUURK"

DUURK = some_function

del some_function

# STILL ABLE TO CALL DUURK
print(DUURK())

# YOU COULD RETURN A FUNCTION FROM A FUNCTION

def some_function_two():

    def some_function_within():
        return "DUUURKUDUUUUURKDUUUUUUUUUUURK"

    return some_function_within

some_function_three = some_function_two()

print(some_function_three())

del some_function_two

print(type(some_function_three()))
print(some_function_three())

# ONE CAN ALSO PASS IN A FUNCTION INTO AN OTHER FUNCTION

def prints_another_function(take_in_another_function):
    print("ANOTHER FUNCTION", take_in_another_function())

prints_another_function(some_function_three)

# HOW DECORATOR LOOKS:

def some_function_four():
    print("FUNCTION FOUR!")

def decorator(old_function):

    def wrapper():

        print("CODE BEFORE OLD FUNCTION")

        old_function()

        print("CODE AFTER OLD FUNCTION")

    return wrapper

decorator(some_function_four)()

# BUT, THIS IS EQUAL TO:

@decorator
def some_function_five():
    print("FUNCTION FUCKING FIVE!")

some_function_five()