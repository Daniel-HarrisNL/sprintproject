import numpy
# Define all of our graphing functions each function asks for the variable inputs
# and use them, along with the range of the graph to plot it

def linear(x):
    # Function used to graph f(x) = a*x + b
    while True:
        try:
            a = float(input("Input the 'a' variable: "))
            b = float(input("Input the 'b' variable: "))
            break
        except:
            print("Error: Invalid input, coefficiencts must be a number.")
    return (a * x) + b

def quadratic(x):
    # Function used to graph f(x) = a*x^2 + b*x + c
    while True:
        try:
            a = float(input("Input the 'a' variable: "))
            b = float(input("Input the 'b' variable: "))
            c = float(input("Input the 'c' variable: "))
            break
        except:
            print("Error: Invalid input, coefficiencts must be a number.")
    return (a * x**2) + (b * x) + c


def cubic(x):
    # Function used to graph f(x) = a*x^3 + b*x^2 + c*x + d
    while True:
        try:
            a = float(input("Input the 'a' variable: "))
            b = float(input("Input the 'b' variable: "))
            c = float(input("Input the 'c' variable: "))
            d = float(input("Input the 'd' variable: "))
            break
        except:
            print("Error: Invalid input, coefficiencts must be a number.")
    return (a * x**3) + (b * x**2) + (c * x) + d


def quartic(x):
    # Function used to graph f(x) = a*x^4 + b*x^3 + c*x^2 + d*x + e
    while True:
        try:
            a = float(input("Input the 'a' variable: "))
            b = float(input("Input the 'b' variable: "))
            c = float(input("Input the 'c' variable: "))
            d = float(input("Input the 'd' variable: "))
            e = float(input("Input the 'e' variable: "))
            break
        except:
            print("Error: Invalid input, coefficiencts must be a number.")
    return (a * x**4) + (b * x**3) + (c * x**2) + (d * x) + e


def exponential(x):
    # Function used to graph f(x) = a*b^(c*x + d)
    while True:
        try:
            a = float(input("Input the 'a' variable: "))
            b = float(input("Input the 'b' variable: "))
            c = float(input("Input the 'c' variable: "))
            d = float(input("Input the 'd' variable: "))
            break
        except:
            print("Error: Invalid input, coefficiencts must be a number.")
    return a * (b**(c*x + d))


def logarithmic(x):
    # Function used to graph f(x) = a*log(b*x + c)
    
    #Check range bounds and return a default value of 1 if boundary is invalid.
    if any(x <= 0):
        print("Error: Range out of bounds for log. Range must be greater than zero.")
        return 1
        
    # Create error handling to prevent logarithm of numbers <= 0
    while True:
        try:
            a = float(input("Input the 'a' variable: "))
            b = float(input("Input the 'b' variable: "))
            c = float(input("Input the 'c' variable: "))
            num = b * x + c
            log = numpy.log(num)
            break
        except:
            print("Error: Invalid input, coefficiencts must be a number.")
    return a * log


def sine(x):
    # Function used to graph f(x) = a*sin(b*x + c)
    while True:
        try:
            a = float(input("Input the 'a' variable: "))
            b = float(input("Input the 'b' variable: "))
            c = float(input("Input the 'c' variable: "))
            num = b * x + c
            sine = numpy.sin(num)
            break
        except:
            print("Error: Invalid input, coefficiencts must be a number.")
    return a * sine


def cos(x):
    # Function used to graph f(x) = a*cos(b*x + c)
    while True:
        try:
            a = float(input("Input the 'a' variable: "))
            b = float(input("Input the 'b' variable: "))
            c = float(input("Input the 'c' variable: "))
            num = b * x + c
            cos = numpy.cos(num)
            break
        except:
            print("Error: Invalid input, coefficiencts must be a number.")
    return a * cos


def squareroot(x):
    # Function used to graph f(x) = a*sqrt(b*x + c)
    
    # Create error handling to prevent input of negative numbers
    while True:
        try:
            a = float(input("Input the 'a' variable: "))
            b = float(input("Input the 'b' variable: "))
            c = float(input("Input the 'c' variable: "))
            if a < 0 or b < 0 or c < 0:
                print("Error: Square root of negative number is not a real number, try again.")
                continue
            num = b*x + c
            sr = numpy.sqrt(num)
            break
        except:
            print("Error: Invalid input, coefficiencts must be a number.")
    return a * sr


def cuberoot(x):
    # Function used to graph f(x) = a*(b*x + c)^(1/3)
    while True:
        try:
            a = float(input("Input the 'a' variable: "))
            b = float(input("Input the 'b' variable: "))
            c = float(input("Input the 'c' variable: "))
            cube = (b*x + c)
            cbrt = numpy.cbrt(cube)
            break
        except:
            print("Error: Invalid input, coefficiencts must be a number.")
    return a * cbrt
    