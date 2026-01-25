import random
number = str (random.randint(10,20))
print("I will pritn a num ber from 10 to 10 and u have to guess the numder one digiht at a time")
print("The game ENDS when u have got 1 point")
while True:
    guess = input("Give me ur best guess")
    if number == guess:
        print("ur won the game")
        print("The number was ",number)
        break
    else:
         print("Ur guess isn't quite rigth try again /n")