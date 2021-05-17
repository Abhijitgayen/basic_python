str1="this is Abhijit Gayen"
print(str1[1:8]) # it print the string str1[1] to str1[7]
print(str1[0])
print("lenth of the array",len(str1))
print(len(str1[1:5]))
# how to write this string completely
print(str1[0:len(str1)+1])
print(str1[0: ])
print(str1[ :len(str1)+1])
# print(str1[0:100]) is allow but print(str1[100]) is not allow
print(str1[0:15:2])
print(str1[ : : ])# this is same as print(str1[: : 1]) and porint(str1 [0:len(styr1)+1 :1])
print( str1[ : : 2]) # it delete  one element in the string i.e str1[1], str[3], str[5], str[7]
print(str1[ : : 3])# it delete two elements scuch that str1[1:3],str1[4:6].....
reverse_str1=str1[ : : -1]
print( "Reverse of the given string is :",reverse_str1)
print(str1[-4:-1])
# 0   1    2    3   4   5   6    7   8   9   10   11   12   13   14   
# t   h    i      s        i    s          A   b   h    i      j      i         t       
#   .... -13 -12 -11 -10 -9   -8  -7  -6 -5   -4   -3     -2      -1

#Some improtent function
print(str1.endswith("gayen"))# output be also a bool
print(str1.count("Ab"))# this be a interger to nuse to count the the the number of sting in this string
print(str1.count("Abk"))
print(str1.count("a"))
print(str1.capitalize()) # this change only the 1 st elemt of the array
print(str1.upper()) 
print(str1.lower())
print(str1.find(" is")) # this give use a integer value it give use the position of this " is" string 
print(str1.find(" isa")) # it will return -1 because this sring is not there  in the main string
print(str1.replace(" is"," are"))
print(str1.isalpha( ))# output be also a bool
