#Program to remove all punctuation from a given string

import string
str1="Goodmoring. welcome everyone! How are you all?"
#Using translate() method - it may replace special characters or remove them altogether

translator = str.maketrans('','', string.punctuation) 


new_string =str1.translate(translator) 

print(new_string)







