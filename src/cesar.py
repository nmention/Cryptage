# function to apply cesarCode to a word
# return the newly translated word
def cesarTranslateWord(word,dec):
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    alphaDico = {}
    i = 0
    for letter in ALPHABET: # Creation of dico : keys = numbers; values = alphabet letters
        alphaDico[i] = letter
        i +=1
    #print(alphaDico)
    wordConversion = []
    for letter in word:
        for key,value in alphaDico.items(): # find keys by values
            if letter in value:
                wordConversion.append(key)
                if len(wordConversion) == len(word):
                    break


    translation = [alphaDico.get((value + dec) % 25) for value in wordConversion] # find the correct letters from the keys
    translation = ''.join(translation)

    return translation

# apply Cesar code to a whole sentence
# return sentence as a str
def translateSentence(sentence,dec):
    sentence = str(sentence)
    sentence = sentence.split()
    translatedSentence = []
    for word in sentence:
        newWord = cesarTranslateWord(word,dec) + " "
        translatedSentence.append(newWord)
    translatedSentence = ''.join(translatedSentence)
    translatedSentence = translatedSentence[0:-2]
    print(translatedSentence)
    return translatedSentence


#TEST
cesarTranslateWord("yes",2)
translateSentence("bonjour je suis noe",2)