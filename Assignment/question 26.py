# program that checks if a string starts with a given prefix or ends with a given suffix

#taking inputs
str=input("Enter the string: ")
yesorno=input("Check prefix or suffix: ")
if yesorno=="prefix" or yesorno=="Prefix" or yesorno=="PREFIX" or yesorno=="suffix" or yesorno=="Suffix" or yesorno=="SUFFIX":
    substring=input("Enter your Prefix: ")
else:
    print("Invalid input")
#checking
if yesorno=="prefix" or yesorno=="Prefix" or yesorno=="PREFIX": 
    if str.startswith(substring)==1:
        print("It's prefix")
    else:
        print("It's not prefix")
if yesorno=="suffix" or yesorno=="Suffix" or yesorno=="SUFFIX":
    if str.endswith(substring)==1:
        print("It's suffix")
    else: 
        print("It's not suffix")

