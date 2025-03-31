import random

choice1, choice2 = input("please enter the players choices: ").split()
main = choice1, choice2
print(main)

if choice1 == choice2:
    print("It's a tie!")
elif choice1 == "rock" and choice2 == "paper":
    print("player2 wins!")
elif choice1 == "rock" and choice2 == "scissors":
    print("player1 wins!")
elif choice1 == "paper" and choice2 == "rock":
    print("player1 wins!")
elif choice1 == "paper" and choice2 == "scissors":
    print("player2 wins!")
elif choice1 == "scissors" and choice2 == "rock":
    print("player2 wins!")
elif choice1 == "scissors" and choice2 == "paper":
    print("player1 wins!")
elif choice1 == choice2:
    print("It's a tie!")
else:
    print("Invalid input!") 

