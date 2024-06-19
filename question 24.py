# program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as
#  input and print the result

#taking inputs
num1=int(input("Enter operand 1: "))
num2=int(input("Enter operand 2: "))
op=input("Enter the operator(arithematic only): ")
#calculating
if op=="+":
    print(num1,op,num2,"=",num1+num2)
elif op=="-":
    print(num1,op,num2,"=",num1-num2)
elif op=="*":
    print(num1,op,num2,"=",num1*num2)
elif op=="/":
    print(num1,op,num2,"=",num1/num2)
else:
    print("Invalid input")