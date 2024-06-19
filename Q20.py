#Program to take a list of numbers and return their sum

list1=[]
n=int(input("Enter number of elements in list: "))
total=0
for i in range(0,n):
    i=int(input("Enter element of list:"))
    list1.append(i)
    total =total + i
            

print(list1)
print("The sum of numbers of the list is: ", total)
    













