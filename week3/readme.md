TODO: Reflect on what you learned this week and what is still unclear.

It's important to think of this not as code, rather as a way to reexpress how I would want to achieve the goal.

#isdigit vs isinstance? 

#except <- throwing and catching>

#\n is what you do when you go to next line i.e ‘Enter Key’

If you want to print something in new line you do like this

print(“Junaid \n Effendi”)
Output:

Junaid
Effendi

#Formatters work by putting in one or more replacement fields or placeholders — defined by a pair of curly braces {} — into a string and calling the str.format()
print("Sammy has {} balloons.".format(5))
Output
Sammy has 5 balloons.

or

open_string = "Sammy loves {}."
print(open_string.format("open source"))
#Don't forget about recalling funcitons 

#ALSO rember the method for defining

def function_name(parameter):

# You can interpolate the target_value into the print string like so:

raise ValueError("{0} not in list".format(target_value))

#also rmbr
you can use 
"if not" for when a lsit is empty

example linear search code via code academy for ur reading

# define your linear_search() below...
def linear_search(search_list, target_value):
  for idx in range(len(search_list)):
    print(search_list[idx])
    if search_list[idx] == target_value:
      return idx
  raise ValueError("{0} not in list".format(target_value))
  
  
# uncomment the lines below to test...
values = [54, 22, 46, 99]
print(linear_search(values, 22))
#notice how here it prints the function with parameters within ooooo

below is another version of linear search now able to account for duplicates
# Search list and target value
tour_locations = [ "New York City", "Los Angeles", "Bangkok", "Istanbul", "London", "New York City", "Toronto"]
target_city = "New York City"

#Linear Search Algorithm
def linear_search(search_list, target_value):
  matches = []
  for idx in range(len(search_list)):
    if search_list[idx] == target_value:
      matches.append(idx)
  if not matches:
    raise ValueError("{0} not in list".format(target_value))
  else:
    return matches

#Function call
tour_stops = linear_search(tour_locations, target_city)
print(tour_stops)


BTW the 
#or
command is a thing

#below is a linear sort that updates the highest value
# Search list
test_scores = [88, 93, 75, 100, 80, 67, 71, 92, 90, 83]

#Linear Search Algorithm
def linear_search(search_list):
  maximum_score_index = None
  for idx in range(len(search_list)):
    if not maximum_score_index or search_list[idx] > search_list[maximum_score_index]:
      maximum_score_index = idx
  return maximum_score_index


# Function call
highest_score = linear_search(test_scores)

#Prints out the highest score in the list
print(highest_score)


//	Floor division - division that results into whole number adjusted to the left in the number line

ie 15//4 = 3 


#eg binary search basic
def binary_search(sorted_list, target):
  if not sorted_list:
    return 'value not found'
  mid_idx = len(sorted_list)//2
  mid_val = sorted_list[mid_idx]
  if mid_val == target:
    return mid_idx
# For testing:
sorted_values = [13, 14, 15, 16, 17]
print(binary_search([], 42))
print(binary_search(sorted_values, 42))
print(binary_search(sorted_values, 15))

#fancy binary
def binary_search(sorted_list, target):
  if not sorted_list:
    return 'value not found'
  mid_idx = len(sorted_list)//2
  mid_val = sorted_list[mid_idx]
  if mid_val == target:
    return mid_idx
  if mid_val > target:
    left_half = sorted_list[:mid_idx]
    return binary_search(left_half, target)
  if mid_val < target:
    right_half = sorted_list[mid_idx+1:]
    result = binary_search(right_half, target)
    if result == "value not found":
      return result
    else:
      return result + mid_idx + 1
# For testing:
sorted_values = [13, 14, 15, 16, 17]
print(binary_search(sorted_values, 16))

#original solution solved the problem of reducing the sorted input list by making a smaller copy of the list.

#This is wasteful! At each recursive call we’re copying N/2 elements where N is the length of the sorted list.

#We can do better by using pointers instead of copying the list. Pointers are indices stored in a variable that mark the beginning and end of a list:

vehicles = ["car", "jet", "camel", "boat"]
start_of_list = 0
end_of_list = len(vehicles)
# 4

vehicles[start_of_list : end_of_list]
# ["car", "jet", "camel", "boat"]

middle_of_list = len(vehicles) // 2
# 2

vehicles[start_of_list : middle_of_list]
# ["car", "jet"]
vehicles[middle_of_list : end_of_list]
# ["camel", "boat"]

# This example copies the list to show what portion is covered
# We won't need to copy in the algorithm!

RMBR THE IDEA THAT THESE CALL THE INDEX 0,1,2,3,4,5...

#def binary_search(sorted_list, left_pointer, right_pointer, target):
  # this condition indicates we've reached an empty "sub-list"
  if left_pointer >= right_pointer:
    return "value not found"
	
  # We calculate the middle index from the pointers now
  mid_idx = (left_pointer + right_pointer) // 2
  mid_val = sorted_list[mid_idx]

  if mid_val == target:
    return mid_idx
  if mid_val > target:
    # we reduce the sub-list by passing in a new right_pointer
    return binary_search(sorted_list, left_pointer, mid_idx, target)
  if mid_val < target:
    # we reduce the sub-list by passing in a new left_pointer
    return binary_search(sorted_list, mid_idx + 1, right_pointer, target)
  
values = [77, 80, 102, 123, 288, 300, 540]
start_of_values = 0
end_of_values = len(values)
result = binary_search(values, start_of_values, end_of_values, 288)

print("element {0} is located at index {1}".format(288, result))"


FINAL ITERATIVE VERSION

def binary_search(sorted_list, target):
  left_pointer = 0
  right_pointer = len(sorted_list)
  
  # fill in the condition for the while loop
  while left_pointer < right_pointer:
    # calculate the middle index using the two pointers
    mid_idx = (left_pointer + right_pointer) // 2
    mid_val = sorted_list[mid_idx]
    if mid_val == target:
      return mid_idx
    if target < mid_val:
      # set the right_pointer to the appropriate value
      right_pointer = mid_idx
    if target > mid_val:
      # set the left_pointer to the appropriate value
      left_pointer = mid_idx + 1
  
  return "Value not in list"

# test cases
print(binary_search([5,6,7,8,9], 9))
print(binary_search([5,6,7,8,9], 10))
print(binary_search([5,6,7,8,9], 8))
print(binary_search([5,6,7,8,9], 4))
print(binary_search([5,6,7,8,9], 6))