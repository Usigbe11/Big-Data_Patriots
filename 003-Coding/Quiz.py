from random import random
for x  in range(30):
    list = [random]


def nameAndID (name, ID):
    return name + ID


def removeDuplicate(objList):
    for x in range(len(objList)):
        for y in range(x+1, len(objList)):
            if objList[x] == objList[y]:
                objList.pop(y)
                return objList


print(removeDuplicate(["sun","mon","sun"]))


def smallestMissingInteger(numList):
    if min(numList) < 0:
        value = min(numList)
        while value <= 0:
            value += 1
        while value in numList:
            value += 1
    return value

    if min(numList) > 0:
        return min(numList)


print(smallestMissingInteger([-1,-2,0,3,5]))
