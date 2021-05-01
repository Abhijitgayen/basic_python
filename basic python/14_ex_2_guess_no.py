n=10
# no of guesses 9
# print the number of guesses
# game over
i=1
while(i<=9):
    gue=int(input(">>>Enter your guess :"))
    if gue!=n and i==8 :
        print ("\t>>>Game over")
    elif gue > n :
        print(">>>Next time batter luck...Enter smaller nuber next time...")
    elif gue < n :
        print(">>>Next time batter luck...Enter greatter nuber next time...")
    elif gue==n :
        print("\t>>> You won this game with guesses :",9-i)
        break
    print(">>>Number of Possible guesses :",9-i)
    i=i+1