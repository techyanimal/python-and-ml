# program to check whether a given number is even or odd

#taking input
num=float(input("Enter the number to be checked: "))
#checking for even or odd
if(num%2==0):
    print("The number {} is Even".format(num))
else:
    print("The number {} is Odd".format(num))