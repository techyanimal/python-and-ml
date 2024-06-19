# program that takes a list of numbers and returns their sum

#taking input
num_lst=[]
while(1):
    num=input("Enter number(only integer): ")
    try: 
      num_lst.append(int(num))
    except  ValueError:  
           print("Your input has been recieved")
           break  
#printing sum
print(num_lst)
sum=0
for i in range(len(num_lst)):
    sum+=num_lst[i]
print("Sum is: ",sum)