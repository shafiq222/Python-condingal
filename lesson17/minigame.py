import random
options = ["rock","paper","siccsiors"]
User_choise =input("Choose rock,paper,siccsiors")
computer_choice = random.choice(options)
print("Ur choice",User_choise)
print("Computer choice",computer_choice)
if User_choise == computer_choice:
    print("Tie")
elif User_choise == "rock" and computer_choice == "siccsiors":
    print("U win!")
elif User_choise == "paper" and  computer_choice == "rock":
    print("U win!")
elif User_choise == "siccsiors" and computer_choice == "paper":
    print("U win!")
else:
    print("U lose :(")