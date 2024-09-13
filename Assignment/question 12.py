# program to calculate sum of digits of a given number

#taking input
num=int(input("Enter the number: "))
#calculating the sum of digits
sum=0
un_d=num%10
while(num):
    sum+=un_d
    num=int(num/10)
    un_d=num%10
print("Sum of digits of given number is ",sum)