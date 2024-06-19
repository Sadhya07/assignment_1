#Program to count the occurences of a specific element in a list
list1=[1,1,2,2,2,3,3,3,4,4,4,4,4,4,5]

def countOccurences(lst, x):
    count=0 
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count
 

# Counting frequency for specific element
num = int(input("Enter element :"))
print("The element {} has occured {} times in the list" .format(num, countOccurences(list1,num)))

#We can also use the count() method
#print(list1.count(5))


















