import random

def mergeSortAlgo(li: list) -> list:
    myli = helper(li, 0, len(li)-1)
    return myli


def helper(li, start, end):

    # Code for leaf node
    if start == end:
        return

    # Internal worker node code
    mid = (start + end) // 2
    helper(li, start, mid)
    helper(li, mid+1, end)

    # merge two sorted halves
    i = start
    j = mid + 1
    aux = []
    while i <= mid and j <= end:
        if li[i] <= li[j]:
            aux.append(li[i])
            i += 1
        else:
            aux.append(li[j])
            j += 1

    while i <= mid:
        aux.append(li[i])
        i += 1

    while j <= end:
        aux.append(li[j])
        j += 1
    li[start: end+1] = aux

    return aux

# Driver Code
myli = [random.randint(1, 100) for i in range(10)]
print(myli)
print(mergeSortAlgo(myli))
