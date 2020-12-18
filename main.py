# Guessing Game where a random number between -10,000 and 10,000
# is generated and the player has to guess that number.

# If the player guesses a number that isn't between -10,000 and 10,000, then
# they get an "OUT OF BOUNDS" message, and if they guess the same number then
# they get a "You've already guessed this number silly!" message.

import random

# randomly generated number between -10,000 and 10,000 that will be guessed for the game
cls=random.randint(-10000,10000)

# numguess holds the current number that the player guesses, and
# lastnumguess holds the number that the player guessed LAST TIME.
numguess=0
lastnumguess=0

# list used to hold all the guess attempts
guesses=[]

# break statement used to break out of loop
while(True):

    # program asks for a number to be inputted and that number is stored into
    # the guesses list
    numguess=int(input("Guess a number between -10,000 and 10,000: "))
    guesses.append(numguess)

    # if number guessed is out of the range
    if(numguess<-10000 or numguess>10000):
        print("OUT OF BOUNDS")
        continue

    # if player guesses the same number that they guessed in the last turn
    elif (numguess == lastnumguess):
        print("You've already guessed this number silly!")

    # on first guess...
    elif(numguess==guesses[0]):

        # if number guessed is within 100 of the random number
        if(numguess-cls<=100 and numguess-cls>=-100):
            print("WARM!")
        # if number guessed is NOT within 100 of the random number
        else:
            print("COLD!")

    # if the current number guessed matches the random number
    elif (numguess == cls):
        break

    # ************************************************************************************
    # This last elif statement is placed at the end to ensure that the ones before it get
    # executed first if their conditional statements are true. Since this elif would
    # be executed 100% of the time on our 2nd guess and onwards without giving the other
    # if/elif statements the chance to execute if it went first, we place it at the end.
    # ************************************************************************************

    # if there has already been a first guess...
    elif(len(guesses)>1):

        # if the current number guessed is closer to the random
        # number than the last number that was guessed
        if(abs(numguess-cls)<abs(lastnumguess-cls)):
            print("WARMER!")
        # if the current number guessed is NOT closer to the
        # random number than the last number that was guessed
        else:
            print("COLDER!")

    # now that we've finished with this try, the current number guessed (numguess)
    # now becomes the last number guessed (lastnumguess) for the next try
    lastnumguess=numguess

    # this print statement is used to put some space between
    # the messages and prompts so they don't get too cluttered.
    print("")

# message to be displayed once you guess the number correctly. Message also
# displays the number of tries that it took to guess the number correctly by
# returning the length of our list.
print("CONGRATULATIONS!!! YOU GUESSED THE NUMBER CORRECTLY AND")
print("IT ONLY TOOK YOU "+str(len(guesses))+" ATTEMPTS TO DO SO!!!")
