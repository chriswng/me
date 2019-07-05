TODO: Reflect on what you learned this week and what is still unclear.

#goals for excercise 1
-read json library and return dictionary
    - last name
        E.g to get the name title you would need to:
         data["results"][0]["name"]["title"]
    password
    number that is postcode +id-value

Hey you got it actually!!
turns out you jsut edit the existing code as it opens the data and "data = json.loads(json_data) is the dictionary?

#why are they using index value 0?
heres why

Open bracket makes the entire json file a dictionay
    The values of results is a list [SQUARE BRACKETS]
        Inside it is a dictionary, thus the first element in that list is the dictionary you're trying to get into.

    while the content in info is pure dictionary


status_code 200 is OK status

#.read vs .readline vs .readlines
    block vs single line vs all the line

Go down into week 4 before testing to really hone in