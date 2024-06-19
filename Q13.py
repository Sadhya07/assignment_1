#Program to ask user for their birth year and calculates their age 

birth_year =int(input("Enter your birth year: "))

from datetime import date

def findAge(birth_year):
    age= (date.today()).year - birth_year
    return age


years= findAge(birth_year)
print("The user is ", years, "years old.")












