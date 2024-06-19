#Program to calculate factorial of number
num=int(input("Enter a number: "))

def factorial(n):
    if n ==0 or n==1 :
        return 1
    else :
        fact=1
        while n>1:
             fact=fact *n
             n=n-1
    return fact

result=factorial(num)
print("Factorial of the given number is: ", result)