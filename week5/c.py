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
            outputword = wordn[2:-1]
                #    this retrives the word from the url
        listwerds.append(outputword) 
    return listwerds


def wordy_pyramid():
    wordlist =[]
    lengths=[3, 5, 7, 9, 11, 13, 15, 17, 19, 20, 18, 16, 14, 12, 10, 8, 6, 4]
    wordlist.extend(list_of_words_with_lengths(lengths))
    return wordlist

print(wordy_pyramid())