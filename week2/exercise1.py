"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ['what', 'does', 'this', 'line', 'do', '?']

#prints the strings in the list some_words
for word in some_words:
    print(word) #it printed the words in the list some_words in a column

#prints the strings in the list some_words
for x in some_words:
    print(x) #it printed the words in the list some_words in a column

#prints the strings in the list some_words
print(some_words) #it printed the list some_words as ['what', 'does', 'this', 'line', 'do', '?']

#prints the strings "some-words contains more than 3 words" in the list some_words as it has a length > 3
if len(some_words) > 3:
    print('some_words contains more than 3 words') #prints "some_words contains more than 3 words"


def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    #it will print out a tuple (round brackets) of identifying information i.e. (ystem, node, release, version, machine, and processor values)
    print(platform.uname()) #it printed 'uname_result(system='Darwin', node='Christophers-MacBook-Air-2.local', release='15.6.0', version='Darwin Kernel Version 15.6.0: Tue Jan  9 20:12:05 PST 2018; root:xnu-3248.73.5~1/RELEASE_X86_64', machine='x86_64', processor='i386')'

usefulFunction()
