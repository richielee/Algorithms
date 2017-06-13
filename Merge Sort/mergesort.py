'''Implementing Merge sort using the conquer and divide method'''


import random

def mergesort(alist):
    '''This is a docstring '''
    if len(alist) > 1:
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

def is_ascending(alist):
    ''' Checks whether a list is ascending'''
    ans = 1
    for i in range(len(alist) - 1):
        ans *= (alist[i] < alist[i + 1])
    return ans

def main():
    '''Main function'''
    # Generate a random list
    alist = random.sample(range(100), 100)
    print("Original list:")
    print(alist)
    mergesort(alist)
    # We can visually inspect whether the list is sorted
    print("Sorted list:")
    print(alist)
    text = lambda i: "That was a list sorted in ascending order" \
    if is_ascending(alist) else "That was rubbish."
    print(text(alist))
if __name__ == '__main__':
    main()
