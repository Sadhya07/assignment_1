#Program to read data from a CSV file and print it to console 

import csv 

with open('firstfile.csv','w',newline='') as file:
    writer =csv.writer(file)
    writer.writerow(["EmpID","EmpName","Salary","department"])
    writer.writerow([101,'Ajay',10000,"Mkt"])
    writer.writerow([102,'Reema',20000,'Prod'])
    writer.writerow([103,'Samar',15000,'Mkt'])

    
with open ('firstfile.csv' ,'r') as file:
    reader=csv.reader(file, delimiter=';',skipinitialspace=True) 
    for row in reader:
        print(row)