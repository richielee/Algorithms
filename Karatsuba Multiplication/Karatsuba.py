'''
A multiplication function that implements the Karatsuba Algorithm
'''

def Karatsuba(x, y):
    if (len(str(x)) == 1 or len(str(y)) == 1):
        return (x * y)
    n = max(len(str(x)), len(str(y)))
    n_half = n/2
    a = x / (10 ** n_half)
    b = x % (10 ** n_half)
    c = y / (10 ** n_half)
    d = y % (10 ** n_half)
    ac = Karatsuba(a,c)
    bd = Karatsuba(b,d)
    mid = Karatsuba(a + b, c + d)  - ac - bd
    return (ac * (10 ** (2 * n_half)) + (mid * (10 ** n_half)) + bd)

def check_multiplication():
    ans = 1
    for i in range(51):
        for j in range(51):
            ans *= (i * j == Karatsuba(i, j))
    return (ans)

print (Karatsuba(3141592653589793238462643383279502884197169399375105820974944592,\
2718281828459045235360287471352662497757247093699959574966967627))
print (check_multiplication())

