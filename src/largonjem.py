# function to determinate if word is suitable for largonjem
# return : Boolean

def jargonCandidate(word):
    voyals = {"a","e","i","o","u","y"}
    if type(word) is not type(str):
        word = str(word)
    if word.isalpha() is False or word[0] in voyals or len(word) < 5:
        return False
    else:
        return True

# apply largonjem to one word
# return the transformed word
def swap(string):
    if jargonCandidate(string) is False:
        message = "{} non traduisible en largonjem"
        print(message.format(string))
        return string

    prefixe = "l"
    buf = string[len(string) - 1]
    string += string[0]
    string = prefixe + string[1:]
    string += "em"
    return string


# apply largonjem to a whole sentence
# return the sentence as a str
def largonSentences(text):
    words = text.split(" ")
    words = [swap(word) for word in words]
        #map(swap,words)
    traduction = " ".join(words)
    return traduction






# TEST
voyelle = {"a,e,i,o,u,y"}
book = "Arma Virumque Cano Trojae Qui Primus Ab Oris"
test = largonSentences(book)
print(largonSentences(book))
print(jargonCandidate("jargon"))
mot = str(input('Entrez votre mot :'))
mot = swap(mot)
print(mot)

