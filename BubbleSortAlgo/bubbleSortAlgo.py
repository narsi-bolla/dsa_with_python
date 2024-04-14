import random

def bubbleSortAlgo(li: list) -> list:
    helper(li)
    return li


def helper(li):
    for i in range(len(li)):
        for redPointer in range(len(li) -1, i, -1):
            if li[redPointer - 1] > li[redPointer]:
                li[redPointer - 1], li[redPointer] = li[redPointer], li[redPointer - 1]
    return li

# DRIVER CODE
myli = [random.randint(1, 100) for i in range(10)]
print(myli)
print(bubbleSortAlgo(myli))