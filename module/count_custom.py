# function 

def count_custom(string,word):
    for i in string.split():
        if i == word :
            yield i