# program that tells whether 2 strings are anagrams of each other or not

#taking input
str1=input("Enter string 1: ")
str2=input("Enter string 2: ")
#checking whether anagram or not
if sorted(str1)==sorted(str2):
    print("Anagrams")
else:
    print("Not anagrams")