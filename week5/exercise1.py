# -*- coding: UTF-8 -*-
"""Refactoring.

This exercise contains a complete and working example, but it's very poorly written.

Your job is to go through it and make it as good as you can.

That means making it self-documenting wherever possible, adding comments where
it isn't. Take repeated code and make it into a function. Also use functions
to encapsulate concepts. If something is done many times, maybe a map or a loop
is called for. Etc.

Some functions will have directions as external comments, once you think you
are on top of it, take these comments out. Others won't have comments and
you'll need to figure out for yourself what to do.
"""




# return a list of countdown messages, much like in the bad function above.
# It should say something different in the last message.
def countdown(message, start, stop, completion_message):
    countlist = []
    #if stop==1:
    for i in range(start-stop+1, stop-stop, -1):
        print(message,str(i))
    print(completion_message)
    return countlist

# TRIANGLES

# This should be a series of functions that are ultimatly used by
# triangle_master
# It should eventually return a dictionary of triangle facts. It should
# optionally print information as a nicely formatted string. Make printing
# turned off by default but turned on with an optional argument.
# The stub functions are made for you, and each one is tested, so this should
# hand hold quite nicely.
def calculate_hypotenuse(base, height):
    hypotenuse = (base**2 + height**2)**(1/2)
    return(hypotenuse)
    


def calculate_area(base, height):
    area = (base*height)/2
    return(area)
    


def calculate_perimeter(base, height):
    perimeter = (base*base + height*height)**(1/2) + base + height
    return(perimeter)
    


def calculate_aspect(base, height):
    aspect = ""
    if height > base:
        aspect = "tall"
    elif base > height:
        aspect = "wide"
    else:
        aspect = "equal"
    return aspect


# Make sure you reuse the functions you've already got
# Don't reinvent the wheel
def get_triangle_facts(base, height, units="mm"):
    return {
        "area": calculate_area(base, height),
        "perimeter": calculate_perimeter(base, height),
        "height": height,
        "base": base,
        "hypotenuse": calculate_hypotenuse(base, height),
        "aspect": calculate_aspect(base, height),
        "units": units,
    }


# this should return a multi line string that looks a bit like this:
#
# 15
# |
# |     |\
# |____>| \  17.0
#       |  \
#       |   \
#       ------
#       8
# This triangle is 60.0mm²
# It has a perimeter of 40.0mm
# This is a tall triangle.
#
# but with the values and shape that relate to the specific
# triangle we care about.
def tell_me_about_this_right_triangle(facts_dictionary):
    tall = """
            {height}
            |
            |     |\\
            |____>| \\  {hypotenuse}
                  |  \\
                  |   \\
                  ------
                  {base}"""
    wide = """
            {hypotenuse}
             ↓         ∕ |
                   ∕     | <-{height}
               ∕         |
            ∕------------|
              {base}"""
    equal = """
            {height}
            |
            |     |⋱
            |____>|  ⋱ <-{hypotenuse}
                  |____⋱
                  {base}"""

    pattern = ( 
        "This triangle is {area}{units}²\n"
        "It has a perimeter of {perimeter}{units}\n"
        "This is a {aspect} triangle.\n"
    )
    area=calculate_area
    perimeter=calculate_perimeter
    aspect=calculate_aspect
    if facts_dictionary["aspect"] == "tall":
        diagram = tall.format(**facts_dictionary)
    elif facts_dictionary["aspect"] == "wide":
        diagram = wide.format(**facts_dictionary)
    else:
        diagram = equal.format(**facts_dictionary)
    facts = pattern.format(**facts_dictionary)
    return( diagram + "\n" + facts)


def triangle_master(base, height, return_diagram=False, return_dictionary=False):
    f=get_triangle_facts(base, height)
    d=tell_me_about_this_right_triangle(f)
    if return_diagram and return_dictionary:
        return {"diagram": d, "facts":f}
    elif return_diagram:
        return d
    elif return_dictionary:
        return f
    else:
        print("You're an odd one, you don't want anything!")


def wordy_pyramid(api_key):
    import requests
    url = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={len}"
    mino = 3
    maxo = 20
    wordlist = []
    templist =[]
    templist2 =[]
    for i in range(mino,maxo+1):
        fullurl=url.format(len=i)
        pull = requests.get(fullurl)   
        if pull.status_code is 200:         
            randword = pull.content  
                #    this retrives the word from the url
            if randword is None: 
                pass
            else:
                randword = str(randword)
                # below checks if the word will have odd or even 
                # no. of characters. Then it sorts them into 
                # separate lists
                if int(i) % 2 ==0:
                    templist2.append(randword[2:len(randword)-1])
                    #  issue with words from this url is that
                    #  they look like --> b'word' 
                    #  so i've applied the range filter as seen above
                    #  and below so to ignore the b' and '
                else:
                    templist.append(randword[2:len(randword)-1])
    templist2.reverse()
    wordlist.extend(templist)
    wordlist.extend(templist2)
    return wordlist
    # baseURL = (
    #     "http://api.wordnik.com/v4/words.json/randomWords?"
    #     "api_key=5586ih53eyafp9iaztwo57zpldgdwwftvv493ppcx0qhno868"
    #     "&minLength={length}"
    #     "&maxLength={length}"
    #     "&limit=1"
    # )
    # pyramid_list = []
    # def loopyloop(x,y,z):
    #     for i in range(x, y, z):
    #         url = baseURL.format(length=i)
    #         r = requests.get(url)
    #         if r.status_code is 200:
    #             message = r.json()[0]["word"]
    #             pyramid_list.append(message)
    #         else:
    #             print("failed a request", r.status_code, i)
    # loopyloop(3,21,2)
    # loopyloop(20,3,-2)    
    # for i in range(20, 3, -2):
    #     url = baseURL.format(length=i)
    #     r = requests.get(url)
    #     if r.status_code is 200:
    #         message = r.json()[0]["word"]
    #         pyramid_list.append(message)
    #     else:
    #         print("failed a request", r.status_code, i)
    # return(pyramid_list)

def not_number_rejector(length):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number 
    (e.g. "cow", "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    given = False

    if not given:
        NUMBER = str(length)
        if NUMBER.isdigit():
            given = True
            return int(NUMBER)
        else: 
            pass

def get_a_word_of_length_n(length):
    import requests
    url = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={leng}"
    if type(length) == int and length >= 3:
        fullurl=url.format(leng=length)
        pull = requests.get(fullurl)   
        if pull.status_code is 200:         
            wordn = pull.content  
            wordn = str(wordn)
            outputword = wordn[2:len(wordn)-1]
                #    this retrives the word from the url
        return outputword
    else:
        return None
    

def list_of_words_with_lengths(list_of_lengths):
    import requests
    listwerds =[]
    url = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={leng}"
    for i in list_of_lengths:
        # if type(i) == int and length >= 3:
        fullurl=url.format(leng=i)
        pull = requests.get(fullurl)   
        if pull.status_code is 200:         
            wordn = pull.content  
            wordn = str(wordn)
            outputword = wordn[2:len(wordn)-1]
                #    this retrives the word from the url
        listwerds.append(outputword) 
    return listwerds
        
    

    baseURL = (
        "http://api.wordnik.com/v4/words.json/randomWords?"
        "api_key=5586ih53eyafp9iaztwo57zpldgdwwftvv493ppcx0qhno868"
        "&minLength={length}"
        "&maxLength={length}"
        "&limit=1"
    )
    n2list =[]
    for i in range(len(list_of_lengths)):
        length=list_of_lengths[i]

        url = baseURL.format(length=length)
        r = requests.get(url)
        
        if r.status_code is 200:
            message = r.json()[0]["word"]
            n2list.append(message)
    return(n2list)


# if __name__ == "__main__":
    # do_bunch_of_bad_things()
    # wordy_pyramid("5586ih53eyafp9iaztwo57zpldgdwwftvv493ppcx0qhno868")
