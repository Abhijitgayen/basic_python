d1={ }
print(type(d1))
d2={"Harry":"Burger","Rohon":"Fish","Skillf":"Ruti","Shubham":{"B":"magie","L":"ruti","D":"chiken"} }# in the dictionary we able to add key as a int , string, float
print(d2["Harry"])
print(d2["Shubham"])
d2["Ankit"]="Junk Food" # add element in the dictionary
d2[42.0]="NOthing"
print(d2)
del d2[42.0] # delete element in the dictionary 
print(d2)
# use of some function in dictionary
d3=d2.copy()
#  del d3["Harry"]
#  print(" d2 is ",d2)
print ( "d3 is", d3)
del d3["Harry"]
print ( " after delete the harry distionaeyd3 is", d3)
del d2["Harry"]
print("after delete the harry distionary is :",d2)
del d2["Shubham"]
print(">>>after delete the shubham d2 distinary is :",d2)
print(">>>try to use the to print only the shubham distinary in th d3",d3.get("Shubham"))
d3.update({"leela" : "she is a hacker"})
print(">>>After all operation d3 is",d3)
print(">>>Print all keys of the distionarys",d3.keys())
print(">>>Print all iteams of d3",d3.items())
# search in google for get more function of distionary