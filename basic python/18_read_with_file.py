# file_O_basic
# "r" -open file for reading -default
# "w"-open file for writting
# "x"-open file if not exists
# "a"-add more content to file (appending in this file)
# "t"-text mode- default
# "b"- binary mode
# "+"-read and write

######### Read Files#######

# f = open("Abhijit_18_file.txt","r") ## you need to write "rt","rb","r"
# content =f.read()
# print(content)
# f.close( )

# f1=open("Abhijit_18_file.txt")
# n_word=f1.read(12)
# print(">>>print frist 12 word:<<<",n_word)
# n_word=f1.read(12)#pont be also present form 1st word to 12 th word
# print(">>>print 2nd 12 word:<<<",n_word)

# f1.close( )
# f2= open("Abhijit_18_file.txt","rt")
# content =f2.read()
# for a in content :
    # print(a)
# this for loop give us all characters in this file


##print all line in files
# f3= open("Abhijit_18_file.txt","r")
# print(">>>Print all lines in this file")
# i=1
# for line in f3:
#     print("\t>>> line ",i,"  :",line)
#     i+=1
# print("\n\n")
# f3.close( )

# #use of readline() function
# f4=open("Abhijit_18_file.txt")
# print(f4.readline())
# print(f4.readline())
# f4.close()

#use of readlines() function
f5=open("Abhijit_18_file.txt")
print(f5.readlines()) #print all lines in a list 
f5.close()