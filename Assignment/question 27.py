# program that converts a string into a list of its characters

#taking input
str=input("Enter your String: ")
#converting
lst=[]
for i in range(len(str)):
    lst.append(str[i])
print("List of characters: ",lst)