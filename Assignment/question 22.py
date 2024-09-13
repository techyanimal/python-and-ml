# program that returns minimum and maximum values in a list of numbers

#taking input
num=list(map(int,input("Enter the number list seperated by space: ").split()))
#finding min and max values
for i in range(0,len(num)):
    if i<len(num)-1:
        if num[i]<num[i+1]:
            min=num[i]
            max=num[i+1]
        else:
            min=num[i+1]
            max=num[i]
    for j in range(i,len(num)):
        if num[j]<min:
            min=num[j]
        if num[j]>max:
            max=num[j]
print("Maximum value: ",max,"\nMinimum value: ",min)