# we try to creat a distionary takeing input form the user
d1={ }
print("Enter key")
a=input();
print("enter word")
b=input();
d1.update({a:b})
print("Enter key")
c=input();
print("enter word")
d=input();
d1.update({c:{a:{b:{a:d}}}})
print(d1)