"""
This is a program to calculate the integral of a square function using
 two methods. The goal is for the result to have a margin error of
  0.001.These assume a lower bound of 0 and a custom upper bound.
 """
# The first method is using the Riemann sum to find the integral
def integrate(function,upperBound,stepSize = 0.0001):
    integral = 0
    x = 0
    while x < upperBound:
        integral += function(x) * stepSize
        x += stepSize

    return integral

# This method creates the function x^2
def square_function(x):
    return x ** 2

# This method calculates the integral using the trapezoidal method
def trapeziodal(function,upperBound,stepSize = 0.001):
    integral = 0
    x = 0
    while x < upperBound:
        trapezoid = (stepSize/2)*(function(x)+function(x+stepSize))
        integral += trapezoid
        x += stepSize
    return integral

# These lines find the integral of x^2 with a lower bound of 0 and upper bound of 5
print(integrate(square_function,5))
print(trapeziodal(square_function,5))
