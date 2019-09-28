#import modules
import random

input("Welcome to the guess the number game. Press enter to start. ")
#loops everything inside until person can follow basic instructions
while True:
    try:
        #checks if the value is a number
        first = int(input("Choose the first number. "))
        break
    except:
        print("Invalid. Choose a number. ")

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
#"correct" is the variable assigned to the random number assigned by randint
#we keep it away from the while loop because otherwise, correct will always be assigned something new.

#now the actual game!
while True:
    while True:
        #first goes through this loop to check if the value is a number
        try:
            guess = int(input("Now guess the number in between. "))
            #"the value can be converted to an integer, so break this loop"
            break
        except:
            print("Not a number. Try again.")
            #the value cannot be converted to an int, and therefore causes a value error. try again.
    
    #now check if the number is correct
    if guess == correct:
        input("Congrats. You guessed the number. Press enter to exit. ")
        break
    elif guess < correct:
        print("Too low. Try again. ")
    else:
        print("Too high. Try again. ")

