# program that converts temperature from Celsius to Fahrenheit and vice versa based on user input

#taking input
temp=float(input("Enter numeric temperature: "))
unit=input("Enter unit(F or C): ")
#converting units
if unit=="F":
    temp_Cel=(temp-32)*5/9
    print("Temperature in Degree Celcius: ",temp_Cel)
else:
    temp_Fah=(temp*9/5)+32
    print("Temperature in Fahrenhiet: ",temp_Fah)
