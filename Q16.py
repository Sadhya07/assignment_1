#Program to count the frequency of each character in a string


# initializing string
str1 = "World Wide Web"
freq = {}
 
for i in str1:
    if i in freq:
        freq[i] =freq[i] +1
    else:
        freq[i] = 1
 
# printing frequency for each character
print("The count of each character present in the string is: \n "
      + str(freq))


