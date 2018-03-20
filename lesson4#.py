'''def min4(a, b, c, d):
    min1 = min(a, b)
    min2 = min(c, d)
    min3 = min(min1, min2)
    return min3


x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())
print(min4(x1, x2, x3, x4))


2  задачи на использование функций


def IsPointInSquare(x, y):
    return -1 <= x <= 1 and -1 <= y <= 1

x = float(input())
y = float(input())
if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')


1 задача на возврат значений


def IsPointInCircle(x, y, xc, yc, r):
    return (x - xc) ** 2 + (y - yc) ** 2 <= r ** 2


x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())
if IsPointInCircle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')

2 задачи на возврат значений

import math


def MinDivisor(n):
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return i
        i += 1
    return n


n = int(input())
print(MinDivisor(n))


import math


def MinDivisor(n):
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return i == n
        i += 1
    return n


def IsPrime(n):
    return n == MinDivisor(n)


n = int(input())
if IsPrime(n):
    print('YES')
else:
    print('NO')


def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n-1)


a = float(input())
n = int(input())
print(power(a, n))

1 задача на рекурсию


def sum(a, b):
    if a == 0:
        return b
    return sum(a-1, b+1)


a = int(input())
b = int(input())
print(sum(a, b))


def exp(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return exp(a ** 2, n // 2)
    else:
        return a * exp(a, n-1)


a = float(input())
n = int(input())
print(exp(a, n))

1  задача на рекурсию

def MaxDivisor(n, m):
    while n != 0 and m != 0:
        if n > m:
            n = n % m
        else:
            m = m % n
    return n + m


def ReduceFraction(n, m):
    i = MaxDivisor(n, m)
    if i == 1:
        return print(n // i, m // i)
    return ReduceFraction(n // i, m // i)


n = int(input())
m = int(input())
ReduceFraction(n, m)


2 задачи на рекурсию

def sumP():
    n = int(input())
    if n != 0:
        return n + sumP()
    return 0


print(sumP())


def rec():
    n = int(input())
    if n != 0:
        rec()
        print(n)
    else:
        print(0)


rec()


'''

import math

def ReduceFraction(n, m)
    while i <= math.sqrt(n):
        if (n % i == 0) and (m % i == 0):
            n = n // i
            m = m // i
            ReduceFraction(n, m)
            return n, m
        i += 1
    return n, m


n = int(input())
m = int(input())
print(ReduceFraction(n, m))


def MaxDivisor(n, m):
    while n != m:
        if n > m:
            n = n - m
        else:
            m = m - n
    return n


def ReduceFraction(n, m):
    i = MaxDivisor(n, m)
    if i == 1:
        return print(n // i, m // i)
    return ReduceFraction(n // i, m // i)


n = int(input())
m = int(input())
ReduceFraction(n, m)