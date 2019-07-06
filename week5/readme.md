TODO: Reflect on what you learned this week and what is still unclear.
In Python strings, the backslash "\" is a special character, also called the "escape" character. It is used in representing certain whitespace characters: "\t" is a tab, "\n" is a newline, and "\r" is a carriage return.

small errors, like having a space within a a set of quotation marks still plagues me.

29

The range function in python has the syntax:

range(start, end, step)

It has the same syntax as python lists where the start is inclusive but the end is exclusive.

So if you want to count from 5 to 1, you would use range(5,0,-1) and if you wanted to count from last to posn you would use range(last, posn - 1, -1).

countdown is troubling in the scenario where it wants a countdown from 4-1 but gives 5 and 2 as inputs
ye haw my math worked eventually

#previously had just d and f for "if return_diagram and return_dictionary:", I didnt realise condition of the test required those labels