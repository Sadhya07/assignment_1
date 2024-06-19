#Program to check if a string starts with given prefix or ends with a given suffix 

str1="Hello everyone! Welcome to class"
prefix= str(input("Enter string to check prefix: "))
print(str1.startswith(prefix))
suffix=str(input("Enter string to check suffix: "))
print(str1.endswith(suffix))



