var1=6
var2=56
var3=int(input(">>>Enter integer :"))
if var3 > var2:
   print(">>>Greater than 56")
elif var3==var3: # short from of elseif
    print(">>>it is equal to 56")
else:
    print(">>> less than 6")
list1=[5,6,8,7,9]
if 9 in list1 :
    print(">>>yes 5 is in this list")
    print (5 in list1)
if 15 not in list1 :
    print(">>>no , 15 is not in this list")
s=set()
s.add(4)
s.add(5)
s.add(48)
print(s)
if 8 in s:
    print(">>> 5 is in this set s")
else:
    print(">>> is not in this set s")


print("Another way to use if and else")
a=14
b=15
print(">>> it is clear that a<b") if a < b  else  print("it is c;lera that b<=a")