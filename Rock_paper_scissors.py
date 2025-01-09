# Rock, Paper, Scissors   which continues to run till the user wins
import random
def chek(user, comp):
    if user == comp:
        return 0
    elif user == 0 and comp == 2:
        return 1
    elif user == 1 and comp == 0:
        return 1
    elif user == 2 and comp == 1:
        return 1
    else:
        return -1

while True :
    comp = random.randint(0,2)
    print("\nChoose 0 -> Rock\n       1 -> Paper\n       2 -> Scissors")
    user = int(input("\nChoose : "))

    print(comp)                                 # printing value chosen by computer also
    score = chek(user, comp)

    if score == 0: print("It's a Draw")
    elif score == 1: print("You WON !!") ;break
    elif score == -1: print("Computer wins")




