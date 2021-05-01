list1=["harray","carry","Larry","Marie"]
for a in list1:
    print(a)
list2=[ ["harry",["cheak",12]],["carry",2],["larry",3],["marry",123]]
print(">>> for loop for list of list")
for item, lolipop in list2:
    print("\t>>>",item,"lolipop is",lolipop)
dict1=dict(list2)
print(dict1)
print(">>>Use for loop in dictionary")
for item, lolipop in dict1.items():
    print("\t>>>",item,"lolipop is",lolipop)
#for geting only key in this dictionary using for loop
print(">>>Only print the key of the dictionary")
for item in dict1:
    print(item)
m=10
# creat a for loop from 0 to m
for i in range(m) :
    print(">>> It is ok see it")

# while loop creat from 0 to m
i=0;
while i<m :
    print(">>>While loop is ok.......")
    i+=1
s=set();
n=int(input("how many element you want to add:"))
for i in range(n):
    a=input("\t>>>Enter element in this set : ")# if we enter the same elemet it will not copy this data
    s.add(a)
print (">>> the setb s is : ",s)
b=input("Enter data to cheack is there in this set: ")
for i in s:
    if i==b :
        print(">>> It is there in this set.....")
        break
    else:
        print(">>>it is not there in this set")
