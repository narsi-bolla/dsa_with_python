import random

def insertionSort(li: list) -> list:
    helper(li)
    return li


def helper(li):
    for i in range(len(li)):
        temp = li[i]
        redPointer = i - 1

        while redPointer >= 0 and li[redPointer] > temp:
            li[redPointer+1] = li[redPointer]
            redPointer-=1
        li[redPointer+1] = temp
    return li


# DRIVER CODE
mylist = [random.randint(1, 100) for i in range(10)]
print(mylist)
print(insertionSort(mylist))