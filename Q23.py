#Program to convert temperature from celsius to Fahrenheit and vice versa based on user input 

check = str(input("Is the entered temperature in celsius?"))
def convertTemp(temp):
 if check == "yes" or "Yes" or "y" or"Y":
     celsius=temp
     fahrenheit = (celsius * 1.8) + 32
     print('%.2f Celsius is equivalent to: %.2f Fahrenheit'% (celsius, fahrenheit))
     return 
 else:
     fahrenheit=temp
     celsius = (fahrenheit-32)/1.8
     print('%.2f Fahrenheit is equivalent to: %.2f Celsius'% (fahrenheit , celsius))
     
     
temp = float(input("Enter temperature :"))
convertTemp(temp)
















