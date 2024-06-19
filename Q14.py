#Program to read multiple lines of input till an empty line and then print them
# Initialize an empty list to store the lines of input 
multiline = [] 
 
# Read input line by line until an empty line is entered 
while True: 
    line = input("Enter a line (leave empty to finish): ") 
    if line: 
        multiline.append(line) 
    else: 
        break 
    
# Join the multiline together with newline characters 
multiline_input = '\n'.join(multiline) 
 
print("Multiline input:") 
print(multiline_input) 














