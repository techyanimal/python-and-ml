# program that reads the contents of a text file and prints it on the console

#opening the file
file=open(r"C:\Users\ANJALI\OneDrive\Documents\practice programs\python programs\text file.txt","r")
#reading and printing from the file
str=file.read()
print("The contents of the file are as follows: ",str)