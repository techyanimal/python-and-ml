# program to calculate factorial of a given number

#taking inout
num=int(input("Enter the nummber: "))
#calculating factorial
fact=1
for i in range(num,1,-1):
    fact*=i
print("Factorial of {} is {}".format(num,fact))
