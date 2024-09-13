# program that asks the user for their birth year and returns their age

from datetime import date 
#taking input
birth_year=int(input("Enter your birth year: "))
#calculating age
cur_yr=date.today()
age=cur_yr.year-birth_year
print("Age: ",age)
