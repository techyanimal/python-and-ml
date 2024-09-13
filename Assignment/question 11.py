# program that generates 1st n numbers in Fibonacci sequence

#taking input
n=int(input("Enter n: "))
#generating 1st n fiboancci numbers
fib=[0,1]
for i in range(2,n):
    fib.append(fib[i-1]+fib[i-2])
print(fib)