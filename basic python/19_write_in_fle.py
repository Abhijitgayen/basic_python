####Write on this file#####
#if there are no file it open this file and write this ijn this file if there are a file  then it also delete all data and write it in this file
f = open("Abhijit_19_file.txt","w")
f.write("Hello it is working.\nReally i am happy to see this .\n\tI able to do this.\n\t\tThank you Harry vai\n")
f.close()


#######Appernding on this file#######
#if there are no file the creat a new file and add those word in this file . if the file exist then add those word at the end of this file no deletion is not happen here 
f1= open("Abhijit_19_file.txt","a")
f1.write(">>>Appending is Done\n\tI able to do this.\n\t\tThank you Harry vai \n")
f1.close()

####Calculate the number of character to write on this file####
f2= open("Abhijit_19_file.txt","a")
a=f2.write(">>>Appending is Done\n\tI able to do this.\n\t\tThank you Harry vai ")
print(">>>no of word print on this file is :",a)
f2.close()
print(">>>done")

#####handel read and write######
f3= open("Abhijit_19_part2_file.txt","r+")
print(">>>case 1>>",f3.read() )
f3.write("\n\tit is ok see it")
print(">>>case2>>",f3.read() )#it is not work becase the ponter is the last position of the set of word
f3.write("\n\tit is ok see it")
f3.close()