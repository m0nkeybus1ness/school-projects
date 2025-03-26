def integrate(function,upperBound,stepSize = 0.0001):
    integral = 0
    x = 0
    while x < upperBound:
        integral += function(x) * stepSize
        x += stepSize

    return integral

def square_function(x):
    return x ** 2

def trapeziodal(function,upperBound,stepSize = 0.001):
    integral = 0
    x = 0
    while x < upperBound:
        trapezoid = (stepSize/2)*(function(x)+function(x+stepSize))
        integral += trapezoid
        x += stepSize
    return integral

print(integrate(square_function,5))
print(trapeziodal(square_function,5))