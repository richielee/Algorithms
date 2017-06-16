'''Count the number of inversions in a list using the divide and conquer method'''


cnt = 0

def inversions(alist):
    '''Perhaps there is a way to avoid using global variable'''
    global cnt
    mid = len(alist) // 2
    left = alist[:mid]
    right = alist[mid:]

    if len(alist) > 1:
        inversions(left)
        inversions(right)

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
                cnt += len(left) - i
            k += 1

        while i < len(left):
            alist[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            alist[k] = right[j]
            j += 1
            k += 1
            cnt += len(left) - i

def main():
    '''Main function'''
    inputfile = open('input.txt', 'r')

    with inputfile as f:
        nbrlst = [int(i.strip()) for i in f.readlines()]
    inversions(nbrlst)
    print(cnt)

if __name__ == '__main__':
    main()

