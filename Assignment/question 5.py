# program that takes a string input from user and writes it to a text file 

#taking input
str=input("Enter your string: ")
#opening the empty file
file=open(r"C:\Users\ANJALI\OneDrive\Documents\practice programs\python programs\text file.txt","w")
#writing in the file
file.write(str)
#closing the file
file.close()
