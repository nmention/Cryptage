message = "Le code de Polype"

alphabet = "A"
binary = ord(alphabet)


def createPolypeSquare():
    superList = []
    listeAlphabet = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                     "U", "V", "W", "X", "Y", "Z"}
    for x in range(5):
        print(listeAlphabet)
        row = (str)(input("Saisissez une ligne du carré de Polype :  "))
        subList = []
        for y in row:
            listeAlphabet.remove(y)
            subList.append(y)

        superList.append(subList)
    return superList


# format the message by putting it all uppercase and stripping blank spaces
# return new str
def formatMessage(string):
    string2 = string.strip()
    string2 = string2.upper()
    a = ""
    newString = string2.split(" ")
    for x in newString:
        a+=x
    return a

def chiffrement(matrix,message):
    msgFormatted = formatMessage(message)
    chiffrage = ""
    for lettre in msgFormatted:
        for i in range(5):
            for j in range(5):
                if lettre == matrix[i][j]:
                    chiffrage += str(i+1) + str(j+1)
    return chiffrage




matrix = [["0" for y in range(5)]for x in range(5)]
for i in range(5):
    for j in range(5):
        matrix[i][j] = chr(binary)
        binary+=1



#TEST
print(createPolypeSquare())
print(matrix)
formatMessage(message)
print(matrix.index(["A","B","C","D","E"]))
print(chiffrement(matrix,message))
