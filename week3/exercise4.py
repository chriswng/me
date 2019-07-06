# -*- coding: UTF-8 -*-
"""Week 3, Exercise 4."""


import math
# import time



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
    """low = 0
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
    """
    tries = 0
  # fill in the condition for the while loop
    while high > low:
        # calculate the middle index using the two pointers
      mid = (low + high)//2
      tries += 1
      if actual_number < mid:
        # set the right_pointer to the appropriate value
        print("Guess number {}: {}".format(tries,mid))
        high = mid 
      elif actual_number > mid:
      # set the left_pointer to the appropriate value
        print("Guess number {}: {}".format(tries,mid))
        low = mid 
      else:
        break
    return {"guess": mid, "tries": tries}

  #MAKE A NEW VARIABLE THAT U BUILD ON
    



if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
