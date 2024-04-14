import random


def selectionSortAlgo(li:list)->list:
    helper(li)
    return li


def helper(li: list) -> list:
    for i in range(len(li)):
        minVal = li[i]
        minInd = i

        for redPointer in range(i+1, len(li)):
            if li[redPointer] < minVal:
                minVal = li[redPointer]
                minInd = redPointer
        li[i], li[minInd] = li[minInd], li[i]
    return li


# DRIVER CODE
myli = [random.randint(1,100) for i in range(11)]
print(myli)
print(selectionSortAlgo(myli))