#Using the Math Module for Calculations

import math

number = float(input("Enter a number: "))
if number >= 0:
    square_root = math.sqrt(number)
    logbase=math.log(number)
    sine=math.sin(number)
else:
    Error = print("Undefined number")

print("Square Root of "+str(number)+" is: "+str(square_root))
print("Logarithm of "+str(number)+" is: "+str(logbase))
print("Sine of "+str(number)+" is: "+str(sine))
