f=open("Abhijit_18_file.txt")
print(f.tell())
print(f.readline())
print(f.tell())
f.seek(0)#seek( 12) is use to put the ponter to the perticuler point of this word
print(f.readline())
print(f.tell())#tell( ) use to find the position of the file pointer
print(f.readline())
f.close()