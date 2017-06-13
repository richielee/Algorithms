"""Implementing Merge sort using conquer and divide"""


import random

def mergesort(alist):
    '''This is a docstring '''
    if len(alist) > 1:
        print("Let's split up the list.")
        mid = len(alist) // 2
        left = alist[:mid]
        right = alist[mid:]

        mergesort(left)
        mergesort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k] = left[i]
                i += 1
            else:
                alist[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            alist[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            alist[k] = right[j]
            j += 1
            k += 1
    print("Merging now")



L = random.sample(range(100), 100)
print(L)
mergesort(L)
print(L)

def is_ascending(alist):
    ''' Checks whether a list is ascending'''
    ans = 1
    for i in range(len(alist) - 1):
        ans *= (alist[i] < alist[i + 1])
    return ans
print(is_ascending(L))
