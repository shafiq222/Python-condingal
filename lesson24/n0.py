import random
import time
number = random.randint(1,100)
def intro():
    print("What is your name")
    global name 
    name = input()
    print(name + "Lets satrt palying a game,I think of number between 1and 100")

    if(number%2==0):
        x="even"
    else:
        x="odd"
    print("this is an",x,"number")
    time.sleep(.5)
    print("GO ahead Guess!")

def pick():
    guessesTaken=0
    while guessesTaken < 6:
        time.sleep(.25)
        enter=input("Guess: ")
        try:
            guess = int(enter)
            if guess <= 100 and guess>=1:
                guessesTaken = guessesTaken+1
                if guessesTaken<6:
                    if guess<number:
                        print("the guess of the number that you have entered is too low")
                    if guess>number:
                        print("the guess of the number that you have entered is too high")
                    if guess != number:
                        time.sleep(.5)
                        print("try agsin")
                    if guess==number:
                        break
            if guess>100 or guess<1:
                print("OMG! Sillyness That number isn't in the range")
                time.sleep(.25)
                print("please enter a number between 1 and 100")
        except:
            print("I don't thik that"+enter+"is a number.Sorry")
    if guess == number:
        print("good job AI",name,"you gussed my number in ",guessesTaken,"guesses")


    if guess != number:

        print('Nope. The number I was thinking of was ' , number)

playagain="yes"

while playagain=="yes" or playagain=="y" or playagain=="Yes":

    intro()

    pick()

    print("Do you want to play again?")

    playagain=input()
