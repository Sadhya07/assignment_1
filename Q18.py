#Program to check if two strings are anagrams of each other 
#Anagram means that all characters of the two strings are the same , only their order may be different 
#For eg.listen and silent , act and cat

str1=str(input("Enter first string: "))
str2=str(input("Enter second string: "))

#Nested ifs
if len(str1)==len(str2):
    
    if sorted(str1)==sorted(str2):
     print("They are anagrams of each other")
    else:
     print("They are not anagrams of each other")

else:
    print("They are not anagrams of each other")