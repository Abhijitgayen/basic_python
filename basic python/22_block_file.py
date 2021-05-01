# f=open("Abhijit_18_file.txt","rt")
# f.close()
#in short we can also write it as 
with open("Abhijit_18_file.txt") as f:
    a=f.read(4)
    print(a)