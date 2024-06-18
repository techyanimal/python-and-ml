# program that counts the frequency of each character in a string

#taking input
str=input("Enter your string: ")
#counting each character
for i in range(0,len(str)):
    ch=str[i]
    count=0
    for j in range(i,len(str)):
        if str[j]==ch:
           count+=1
    print("Frequency of character ",ch,"is ",count)