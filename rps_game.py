import sys
user1=input("whats your name?  ")
user2=input("And your name..?  ")
user1_answer= input("%s do you want choose rock,paper  or scissors?: " % user1)
user2_answer= input("%s do you want choose rock,paper  or scissors?: " % user2)
def compare(u1,u2):
    if u1==u2:
        print("It's a tie!")
    elif u1=='rock':
        if u2=='scissors':
            print (user1," wins")
        else:
            print (user2, " wins")
    elif u1 == 'scissors':
        if u2 == 'paper':
            print(user1, " wins")
        else:
            print(user2, " wins")
    elif u1 == 'paper':
        if u2 == 'rock':
            print(user1, " wins")
        else:
            print(user2, " wins")
    else:
        print("  Invalid input ! you have entered rock,paper or scissors ,try again.")
        sys.exit()


print(compare(user1_answer , user2_answer))