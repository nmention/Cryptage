import math
import sys



def cribleErastothen(N):
    liste = []
    liste2 = []
    for i in range(2, N):
        liste.append(i)

    for i in liste:
        if i == liste[len(liste) - 1]:
            break
        if i > math.sqrt(N):
            break
        liste2 = liste[liste.index(i) + 1:]
        for j in liste2:
            if (j % i == 0):
                liste.remove(j)

    print(liste)
    return liste


def findTwinsPrime(primeList):
    primeList.sort()
    twinsPrimeListe = []
    for i in range(2,len(primeList)-1):
        if primeList[i+1] - primeList[i] <= 2:
            twinsPrimeListe.append(primeList[i])
            twinsPrimeListe.append(primeList[i+1])
    print(twinsPrimeListe)
    return twinsPrimeListe
def coloration(liste):
    listColor = ["red","blue","yellow","green","cyan","magenta","purple","pink","orange","brown","black"]
    listValue = []
    coloredList = []
    temp = liste[0]
    iterator = iter(listColor)
    for i in range(1,len(liste)-1):
        if liste[i] >= temp + 3:
            listValue.append(liste[i])
            listValue.append(next(iterator))
            coloredList.append(listValue)
            listValue = []
            print(coloredList)
            temp = liste[i]
    return coloredList




findTwinsPrime(cribleErastothen(89))
coloration(cribleErastothen(89))


