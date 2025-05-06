#Task 1: Calculate Factorial Using a Function

Number=int(input("Please enter a number: "))
def factorial(n):
    if n<2:
        if n==2:
            return 2
        else:
            return 1
    else:
        return n * (factorial(n-1))
finaloutput=factorial(Number)
print("Factorial of "+str(Number)+" is: "+str(finaloutput))
