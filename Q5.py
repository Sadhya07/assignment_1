#Program that takes string input from user and writes it to text file

str1=input("Enter any string: ")

file1 =open('C:/Users/acer/OneDrive/Desktop/coding/program.txt','w')
print(str1,end='!!',file=file1)