import math


def stringToAscii(string):
    return [ord(character) for character in string]

def cryptRsa(message,c,n):
    asciiMess = stringToAscii(message)
    asciiMess = [math.pow(element,c) for element in asciiMess]
    asciiMess = [element % n for element in asciiMess]
    asciiMess = [int(element) for element in asciiMess]
    return asciiMess

def decryptRsa(x,d,n):
    message = [math.pow(element,d) % n for element in x]
    message = [int(element) for element in message]
    #message = [chr(element) for element in message]
    return message


def pgcd(a, b):
    if b > a:
        temp = b
        b = a
        a = temp
    if b == 0:  # pgcd
        return a
    while a % b != 0:
        temp = a
        a = b
        b = temp % b

    return b


def generateKeys():
    p = 2
    q = 7
    c = 0
    n = p * q
    indEuler = (p-1)*(q-1)
    for i in range(2,indEuler,1):
        if pgcd(i,n) == 1 and pgcd(i,indEuler) == 1:
            c = i
    print(c)
    d = 1
    compteur = 0
    while d * c % indEuler != 1 or compteur < 1:
        if d * c % indEuler == 1:
            compteur += 1
        d +=1

    print(n)
    print(indEuler)
    print(d)
    return [(c,n),(d,n)]






generateKeys()
crypt = cryptRsa("Hello",generateKeys()[0][0],generateKeys()[0][1])
print(crypt)
decrypt = decryptRsa(crypt,generateKeys()[1][0],generateKeys()[1][0])
print(decrypt)




