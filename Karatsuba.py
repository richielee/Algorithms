'''
A multiplication function that implements the Karatsuba Algorithm
As we aim to process very large numbers, the output should be of type string.
'''

def strplus(x, y):
    ans = ''
    n = max(len(x),len(y))
    x = '0' * (n - len(x)) + x
    y = '0' * (n - len(y)) + y
    x = x[::-1]
    y = y[::-1]
    i = 0
    carry = 0
    while (i < n):
        tmp = int(x[i]) + int(y[i]) + carry
        if (tmp > 9):
            tmp -= 10
            carry = 1
        else:
            carry = 0
        ans += str(tmp)
        i += 1
    if (carry):
        ans += str(carry)
    return (ans[::-1])

def strminus(x, y):
    pass

def check_plus():
    ans = 1
    for i in range(510):
        for j in range(510):
            ans *= (i + j == int(strplus(str(i),str(j))))
    return (ans)
print (check_plus())

def Karatsuba(x, y):
    n = len(x)
    if (n == 2):
        return (str(int(x) * int(y)))
    a = x[:n/2]
    b = x[n/2:]
    c = y[:n/2]
    d = y[n/2:]
    ac = Karatsuba(a,c)
    bd = Karatsuba(b,d)
    a_b = strplus(a, b)
    c_d = strplus(c, d)
    abcd = Karatsuba(a_b, c_d)
    mid = strminus(strminus(abcd, ac), bd)
    print('abcd',abcd)
    print('ac', ac)
    print('bd',bd)
    return (strplus(strplus((ac + '0' * n) , (mid + '0' * (n/2))), bd))



