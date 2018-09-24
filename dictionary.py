import json
from difflib import get_close_matches
'''this is a library difflib which has a get_close_matches which takes argument 1. word
to be macthed and 2. from the list of words it returns list of word which has ratio
more than given ratio and the first word is highestt matched word or string
'''


def meaning(word):                      #fuction to find meaning
    if word[0].isupper() == True:
        if word[1:].islower() == False:
            word=word.lower()
            
    if word in data:                        
        return(data[word])

        ''' we can use this also in case of 1st if
        elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]           '''
    
    elif len(get_close_matches(word,data.keys()))>0 :   #if words matches and retured list has items more thann zero
        match= get_close_matches(word,data.keys())[0]   #accesing the first matched word
        yesno=input( "did you mean \"%s\" instead . press Y if yes or N if no  :  " %match)
        if yesno=="Y" or yesno == "y":
            return(data[match])
        elif yesno == "N" or yesno=="n":
            return "the word doesn't exist. please recheck it "
        else:
            return "we didn't understand your query"
    else:
        return " the word doesn't exist . please recheck it"

data= json.load(open("data.json"))  #json library std has a method load which takes file object and returns dictionary

word=input("enter any word  : ")
mean=meaning(word)

if type(mean)==list:
    for item in mean:
        print("------",item)
else:
    print(mean)





