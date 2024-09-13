# program that copies the contents of one text file to another

#opening files
file1=open(r"C:\Users\ANJALI\OneDrive\Documents\practice programs\python programs\Python and ml assignment 1\text file.txt","r")
file2=open(r"C:\Users\ANJALI\OneDrive\Documents\practice programs\python programs\Python and ml assignment 1\text file 0.2.txt","w")
#copying
text=file1.read()
file2.write(text)
#closing files
file1.close()
file2.close()
