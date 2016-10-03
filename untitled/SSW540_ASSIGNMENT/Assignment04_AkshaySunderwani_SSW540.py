# SSW 540 - Assignment 04 - P4: Guess a Number using loops and a function
# Akshay Sunderwani

import random

# handle user guess with guessed number
def startguess(userinput , guessed):
    if userinput > 20 or userinput < 0:
        return 2
    if userinput > guessed:
        return 1
    elif userinput < guessed:
        return -1
    elif userinput == guessed:
        return 0


# method to start the game and handle user tries and its check with guessed number
def startthegame():
    print ( "\tWelcome to 'Guess My Number'!\n" )
    name = input ( "Hello! What is your name? " )

    # max range for number selection, and max number of tries
    max_range = (1 , 20)
    max_tries = 6
    guessednumber = random.randint ( *max_range )

    print ( "Well, " , name , ', I\'m thinking of a number between %d and %d.' % max_range )

    for tries in range ( max_tries ):
        try:
            guess = int ( input ( "Take a guess: " ) )
            check = startguess ( guess , guessednumber )

            if check == -1:
                print ( "Your guess is too low." )
            elif check == 1:
                print ( "Your guess is too high." )
            elif check == 0:
                print ( "Good job, " , name , ", you guessed my number in " , tries + 1 , "guesses!" )
                break
            elif check == 2:
                print ( "The number is between %d and %d." % max_range )
        except:
            print ( "Please enter a valid guess." )

    else:
        print ( "The number I was thinking of was " , guessednumber , "!\n\n" )

    try:
        input ( "Press the enter key to exit." )
    except:
        pass


startthegame ( )
