# if  num is even 
# * * * * * 
# * * * *
# * * *
# * *
# *
# if num is odd
# *
# * *
# * * *
# * * * * 
# * * * * *


n=5
while 1:
    num=int(input("Enter the number :"))
    if num%2==0 :
        for i in range(n):
            for j in range(n-i):
                print("\t*",end= '  ')
            print("\n")
    elif num%2==1 :
        for i in range(n):
            for j in range(i+1):
                print("\t*",end= '  ')
            print("\n")
    op=input("Are you want to continue ?(y/n)")
    if(op=="n"  or op=="N") :
        print(">>>Terminating................")
        break