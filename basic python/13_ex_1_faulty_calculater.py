#faulty Calulater
# 45*3=555 , 56+9 =77 , 56/6=4
while(1):
    num1=int(input(">>>Enter the 1st Number:"))
    num2=int(input(">>>Enter the 2Nd NUmber:"))
    op=input(">>>Whice operation you want ? '+' / '-'/ '*'/ '/ ' :")
    if  num1==45 and num2==3 and op=='*':
        print("\t>>> Anser is :",555)
    elif  num2==45 and num1==3 and op=='*':
        print("\t>>> Anser is :",555)
    elif  num1==56 and num2==9 and op=='+':
        print("\t>>> Anser is :",77)
    elif  num2==56 and num1==9 and op=='+':
        print("\t>>> Anser is :",77)
    elif  num1==56 and num2==6 and op=='/':
        print("\t>>> Anser is :",4)
    elif  num2==56 and num1==6 and op=='/':
        print("\t>>> Anser is :",4)
    else:
        if op=='*':
            print("\t>>> Anser is :",num1*num2)
        elif op=='+':
            print("\t>>> Anser is :",num1+num2)
        elif op=='-':
            print("\t>>> Anser is :",num1-num2)
        elif op=='/':
            print("\t>>> Anser is :",num1/num2)
    con=input(">>>Enter y / n to calculate again :")
    if(con=='n' and con=='N'):
        break