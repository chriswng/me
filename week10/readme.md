TODO: Reflect on what you learned this week and what is still unclear.

#Last lecture

Dealing with python in rhino 
Grasshopper is a visual programming engine for rhino


--check out what booleon indexing in a pandas dataframe does
"import rhinoscriptsyntax as rs"

#USING NOTEBOOK AS PRESENTATION
"pip install RISE"
- after restarting notebook there will be a little button for you to convert to slideshow mode.


#THIS IS CALLED SLICING
"print ("\n [:10] -->", pets[:10])"
"print ("\n [::-1] -->", pets[::-1])"

#Append vs Extend
- appending a list to a list -> it goes in as a list
- extending a list with a list -> goes in as items into the list

#Truthy values
- 0, False, None and empty list [] are Falsey values

#List comprehension trick
- instead of list = []
for i in list2:
    list.append(len(i))

- we can use
lenlist = [len(p) for p in pets]
and even keep going lenlist = [len(p) for p in pets if "c" in p]
- imagine possibilities
- [x*2 for x in range(3)]

#lambdas
- (not directly relevat ut imagine 
def get2xlength(mystring) 
    return len(mystring)*2)

print(list(map(get2xlen, pets)))

this can be redone by print (list(map(lambda x: len(x) * 2, pets)))
print (list(map(lambda x: x[1], pets)))

#built ins
from random import randint
list = [randint(0,100) for _ in range(1000)]
- max(list) = 100
- min(list) = 0
- list(zip(range(len(pets)), pets))
    zips two things together
    list is used to visualise it

for p in enumerate(pets):
    print(p)
- takes the list and adds an index to it
for i, p in enumerate(pets):
    print(i,p)
- now the index and pets are separated

#Generator
generators in python2.x would output a list (e.g. range() is a generator). In 3.x they are stored and save memory
after a = enumerate(pets)

you can use print(next(a))
- creates a kind of loop where it continuously prints the next element

"yield" - look into it


#dictionary comprehensions
L= range(10)
d = {k:v for k,v in zip(pets, L)}
print (d)
\
what this gets is a dicitonary with "k" : v where k is the first elements pets and then v is L
