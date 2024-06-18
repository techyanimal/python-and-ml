# program that removes all punctuations from a given string

#taking input
str=input("Enter your string: ")
#defining punctuation
punc='''"!@#$%^&*()_:;"'?/.,"'''
#removing punctuation
str0=""
for i in range(0,len(str)):
    if str[i] not in punc:
        str0+=str[i]
    else:
        continue
print("Output string: ",str0)