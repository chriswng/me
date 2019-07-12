"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random

def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number 
    (e.g. "cow", "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    given = False

    while not given:
        NUMBER = str(input(message))
        if NUMBER.isdigit():
            given = True
            return int(NUMBER)
        else: 
            print("Numbers only here! (no special characters)")

def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    print("\nWelcome to the guessing game!")
    print("A number between _ and _ ?")

    #lowerBound = input("Enter an lower bound: ")
    lowerBound = not_number_rejector("Enter a lower bound: ")

    #upperBound = input("Enter an upper bound: ")
    upperguess = False
    while not upperguess:
      upperBound = not_number_rejector("Enter an upper bound: ")
      if upperBound > lowerBound:
         upperguess = True
      else:
        print("HEY YOU SET THE BOUNDS SO STAY WITH IT")


    print("OK then, a number between {} and {} ?".format(lowerBound, upperBound))
    lowerBoundcour = int(lowerBound)
    upperBoundcour = int(upperBound)

    actualNumber = random.randint(lowerBoundcour, upperBoundcour)

    guessed = False

    while not guessed:
      guessedNumber = not_number_rejector("Make a guess: ")
      print("You guessed {},".format(guessedNumber),)
      if guessedNumber == actualNumber:
        print("You got it!! It was {}".format(actualNumber))
        guessed = True
      elif guessedNumber < lowerBoundcour:
        print("HEY YOU SET THE BOUNDS SO STAY WITH IT")
      elif guessedNumber > upperBoundcour:
        print("HEY YOU SET THE BOUNDS SO STAY WITH IT")
      elif guessedNumber < actualNumber:
        print("Too small, try again :'(")
      else:
        print("Too big, try again :'(")
 

    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
