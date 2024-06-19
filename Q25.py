#Program to copy the content of one text file into another
# open both files together

with open('first.txt','r') as firstfile, open('second.txt','a') as secondfile: 
      
    # read content from first file 
    for line in firstfile: 
               
             # write content to second file 
             secondfile.write(line)


  






