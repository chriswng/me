# -*- coding: UTF-8 -*-
"""Week 3, Exercise 4."""


import math
# import time

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

def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.
    
    Each guess, print what the guess is. Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}
    
    This will be quite hard, especially hard if you don't have a good diagram!
    
    Use the VS Code debugging tools a lot here. It'll make understanding 
    things much easier.
    """
    low = 0
    high = 0
  
    low = not_number_rejector("Enter a lower bound: ")

    #upperBound = input("Enter an upper bound: ")
    upperguess = False
    while not upperguess:
      high = not_number_rejector("Enter an upper bound: ")
      if high > low:
         upperguess = True
      else:
        print("HEY YOU SET THE BOUNDS SO STAY WITH IT")

    #sorted_list = list(range(low,high))
    
    tries = 0
    guess = 0
    guessed = False
  # fill in the condition for the while loop
    while not guessed:
        # calculate the middle index using the two pointers
        mid = (low + high)//2
        if mid == actual_number:
            print("The number {} has been found!".format(mid))
            guess = actual_number
            guessed = True
        elif actual_number < guess:
        # set the right_pointer to the appropriate value
            tries = int(tries) + 1
            print("Guess number {}: {}".format(tries,mid))
            high = guess
        else:
        # set the left_pointer to the appropriate value
            tries = int(tries) + 1
            print("Guess number {}: {}".format(tries,mid))
            high = guess + 1
    return {"guess": guess, "tries": tries}

  #MAKE A NEW VARIABLE THAT U BUILD ON
    



if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
