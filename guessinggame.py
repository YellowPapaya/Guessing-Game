#import modules
import random

input("Welcome to the guess the number game. Press enter to start. ")
#loops everything inside until person can follow instructions
while True:
    try:
        #checks if the value is a number
        first = int(input("Choose the first number. "))
        break
    except:
        print("Invalid. Choose another. ")
while True:
    try:
        #checks if the value is a number and is larger than first.
        second = int(input("Now choose the second number. "))
        if second >= first:
            break
        else:
            print("Second number cannot be less than the first number.")
    except:
        print("Invalid. Choose another. ")

correct = random.randint(first, second)
while True:
    while True:
        try:
            guess = int(input("Now guess the number in between. "))
            break
        except:
            print("Not a number. Try again.")
    if guess == correct:
        input("Congrats. You guessed the number.")
        break
    elif guess < correct:
        print("Too low. Try again. ")
    else:
        print("Too high. Try again. ")