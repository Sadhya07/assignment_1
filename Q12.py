#Program to calaculate the sum of digits of given number

num =int(input("Enter a number: "))

def findsum(n):
  sum=0
  while n>0 :
      sum = sum + (n%10)
      n=n //10
      
  return sum
    
result =findsum(num)
print("The sum of digits of given number is: ", result) 
    
    
    




