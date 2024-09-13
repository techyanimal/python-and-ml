# program that counts the occurences of a specific element in  a list

#taking input
lst=list(input("Enter your list: ").split())
#counting occurences
ele=input("Enter the specific element: ")
count=0
for i in lst:
    if i==ele:
        count+=1
print("The number of occurences of ",ele,"in the list is ",count)