# program to take multiple line input from user untill a new line is added 

lines=[]
while(1):
    single_line=input("Enter lines: ")
    if single_line=="":
        break
    lines.append(single_line)
#confirming if worked
print(lines) 