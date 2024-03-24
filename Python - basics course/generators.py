# RANGE IS GENERATOR: ONLY LAST NUMBER RETURNED AND STEPSIZE IS MEMORIZED, BUT NOT A WHOLE LIST, WHICH WOULD WASTE MEMORY
# KEYWORD USED IS YIELD INSTEAD OF RETURN
# LAZY EVALUATION!!!

# DIFFERENCE:

def powerfunction(n):

    a = []

    for i in range(n):
        a.append(i**4)

    return a

print(powerfunction(5))

def power_function_generator(n):

    for i in range(n):
        yield i**5

print(list(power_function_generator(7)))

for i in power_function_generator(6):
    print("THIS IS: ",i)


# GENERATING FIBONNACI:

def fib(n):

    xn = 1
    xnplus = 1

    for i in range(n):
        yield xn
        xn , xnplus = xnplus , xn + xnplus

print(list(fib(9)))

huh = fib(9)

print(next(huh),next(huh),next(huh),next(huh),next(huh),next(huh),next(huh),next(huh),next(huh))

