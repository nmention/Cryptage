import math


def pgcd(a, b):
    if b > a:
        temp = b
        b = a
        a = temp
    if b == 0:  # pgcd
        return a
    while a % b != 0:
        b = a % b
        a = b
    print(b)
    return b


def ppcm(a, b):
    print(a * b / pgcd(a, b))
    return (a * b) / pgcd(a, b)


def decToBinary(n):
    binary = ""
    while n != 0:
        binary += str(n % 2)  # convert decimal into to string binary
        n = n // 2
    binary = binary[::-1]
    print(binary)
    return binary


def findValueToBinary(binary):
    indice = len(binary) - 1
    liste = []
    for c in binary:
        if c == "1":
            liste.append(int(c) * math.pow(2, indice))  # decomposition of binary string into decimal
        indice -= 1
    print(liste)
    return liste


def processPower(x, exposant):
    result = 1
    exposant = decToBinary(exposant)
    liste = findValueToBinary(exposant)  # calculate power with the decomposition of binary
    for e in liste:
        result *= math.pow(x, e)
    print(result)
    return result


pgcd(30, 20)
pgcd(12, 15)
ppcm(12, 15)
decToBinary(3)
decToBinary(173)
findValueToBinary(decToBinary(100))
processPower(2, 10)
