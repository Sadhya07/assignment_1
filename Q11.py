#Program to generate the first n numbers in the fibonacci series 

num=int(input("Enter a number to generate the fibonacci series: "))

def fibonacci(n):
    n1=0
    n2=1
    if n<1:
        print("Invalid input")
        return
   
    print(n1)
    for i in range(1,n):
        print(n2)
        fib =n1 +n2
        n1=n2
        n2=fib
#calling the function for given input
fibonacci(num)        
        











