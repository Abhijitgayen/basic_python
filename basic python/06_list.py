myList=["it","is","see","now","by","abhijit", "gayen","ram","shyam",12] # in my list i will be able to store  string,integer, floating point,
print(myList)
print(myList[5])# using index we able to find the exactly the string
myNumber=[12,15,14,1,2,3,-50,158,123,12]
print("my list is ",myNumber)
print("max in list ",max(myNumber),"\nmin of this list is ", min(myNumber))
myNumber.sort()
print("my list after sorting",myNumber)
myNumber.reverse ()
print("After reversing this myList is :",myNumber)
print(myNumber[1:6])
print(myNumber[ : : -1])# we see allthing in the string
myNumber.append( 123)# add this number in the end of this list
print(myNumber)
myNumber.insert( 0,156)# insert the elemt at the position of index 0
print(" Insert element in this list we get",myNumber)
myNumber.remove(1)
print("after removing the element  1 in list ", myNumber)
myNumber.pop()#remove the last element of this list
# Mutable --can change
#Immutable --Cannot change
tp=(1,45,12)
print(tp)
# tp[0]=12 not ran rhis portion because this is a immutable
#how to swap two elelment in the python
a=123
b=45
a,b=b,a
# temp=a
# a=b
# b=temp
print(a,b)