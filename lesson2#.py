#a = int(input())
#b = int(input())
#if a <= b:
#    print(b)
#else:
#    print(a)


#a = int(input())
#b = int(input())
#if a > b:
#    print(1)
#elif a < b:
#    print(2)
#else:
#    print(0)


#a = int(input())
#b = int(input())
#c = int(input())
#if a > b:
#    max = a
#else:
#    max = b
#if max > c:
#    print(max)
#else:
#    print(c)


#x1 = int(input())
#y1 = int(input())
#x2 = int(input())
#y2 = int(input())
#if abs(x2 - x1) <= 1 and abs(y2 - y1) <= 1:
#    print('YES')
#else:
#    print('No')


#x = int(input())
#y = int(input())
#if y % (y - x + 1) == 0:
#    print('YES')
#else:
#    print('NO')


#x1 = int(input())
#y1 = int(input())
#x2 = int(input())
#y2 = int(input())
#if (x1 + y1 + x2 + y2) % 2 == 0:
#    print('YES')
#else:
#    print('NO')


'''n = int(input())
m = int(input())
k = int(input())
if ((k % m == 0) and (k // m < n)) or ((k % n) == 0 and (k // n < m)):
    print('YES')
else:
    print('NO')'''

'''n = int(input())
t = n % 10
if t == 1 and n != 11:
    print(n, 'korova')
elif 2 <= t <= 4 and n // 10 != 1:
    print(n, 'korovy')
else:
    print(n, 'korov')'''


'''x = int(input())
if x > 0:
    print(1)
if x == 0:
    print(0)
if x < 0:
    print(-1)'''


'''x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
xS = x1 * x2
yS = y1 * y2
if (xS > 0) and (yS > 0):
    print('YES')
else:
    print('NO')'''

'''x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if y2 > y1:
    if (x1 + x2 + y1 + y2) % 2 == 0:
        if x2 - x1 <= y2 - y1:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')'''


'''a = int(input())
b = int(input())
c = int(input())
if (a + b <= c) or (a + c <= b) or (b + c <= a):
    print('impossible')
elif (c**2 == a**2 + b**2) or (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2):
    print('rectangular')
elif (c**2 < a**2 + b**2) and (a**2 < b**2 + c**2) and b**2 < (a**2 + c**2):
    print('acute')
else:
    print('obtuse')'''


'''a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if a > b:
    (a, b) = (b, a)
if a > c:
    (b, c) = (c, b)
if a > b:
    (a, b) = (a, b)
print('a, b, c')
'''

'''a = int(input())
b = int(input())
c = int(input())
if a * b * c % 2 == 0:
    if a % 2 != 0 or b % 2 != 0 or c % 2 != 0:
        print('YES')
    else:
        print('NO')
else:
    print('NO')'''

'''a = int(input())
b = int(input())
c = int(input())
if a == b or b == c or a == c:
    if a == b and b == c:
        print('3')
    else:
        print('2')
else:
    print('0')'''

'''a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if a <= d and b <= e or a <= e and b <= d:
    print("YES")
elif c <= d and b <= e or c <= e and b <= d:
    print("YES")
elif c <= d and a <= e or c <= e and a <= d:
    print("YES")
else:
    print("NO")
'''

'''a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
if a1 > b1:
    (a1, b1) = (b1, a1)
if b1 > c1:
    (b1, c1) = (c1, b1)
if a1 > b1:
    (a1, b1) = (b1, a1)
if a2 > b2:
    (a2, b2) = (b2, a2)
if b2 > c2:
    (b2, c2) = (c2, b2)
if a2 > b2:
    (a2, b2) = (b2, a2)
if a1 == a2 and b1 == b2 and c1 == c2:
    print('Boxes are equal')
elif a1 <= a2 and b1 <= b2 and c1 <= c2:
    print('The first box is smaller than the second one')
elif a1 >= a2 and b1 >= b2 and c1 >= c2:
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')'''


'''a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
x1 = (a1 // a2) * (b1 // b2) * (c1 // c2)
x2 = (a1 // a2) * (b1 // c2) * (c1 // b2)
x3 = (a1 // b2) * (b1 // c2) * (c1 // a2)
x4 = (a1 // b2) * (b1 // a2) * (c1 // c2)
x5 = (a1 // c2) * (b1 // b2) * (c1 // a2)
x6 = (a1 // c2) * (b1 // a2) * (c1 // b2)
if x1 >= x2 and x1 >= x3 and x1 >= x4 and x1 >= x5 and x1 >= x6:
    print(x1)
elif x2 >= x1 and x2 >= x3 and x2 >= x4 and x2 >= x5 and x2 >= x6:
    print(x2)
elif x3 >= x1 and x3 >= x2 and x3 >= x4 and x3 >= x5 and x3 >= x6:
    print(x3)
elif x4 >= x1 and x4 >= x2 and x4 >= x3 and x4 >= x5 and x4 >= x6:
    print(x4)
elif x5 >= x1 and x5 >= x2 and x5 >= x3 and x5 >= x4 and x5 >= x6:
    print(x5)
elif x6 >= x1 and x6 >= x2 and x6 >= x3 and x6 >= x4 and x6 >= x5:
    print(x6)'''

'''k = int(input())
if k < 3 or k == 4 or k == 7:
    print('NO')
else:
    print('YES')'''

4 задачи на if


'''n = int(input())
i = 1
x = 1
while x <= n:
    x = i ** 2
    if x <= n:
        print(x, end=' ')
    i = i + 1
или
n = int(input())
i=1
while i ** 2 <= n: 
    print(i ** 2, end=' ')
    i = i + 1     
'''

'''now = int(input())
nowMin = now
i = 2
while 2 <= i <= now:
    if now % i == 0:
        nowMin = i
        print(nowMin)
        break
    else:
        i = i + 1
        
или

n = int(input())
i = 2
while n % i != 0:
    i = i + 1
print(i)
'''
3 задачи на while

'''x = float(input())
y = float(input())
s = x
i = 1
while s < y:
    s = 1.1 * s
    i = i + 1
print(i)
'''

'''now = int(input())
nowMax = 0
while now != 0:
    if now >= nowMax:
        nowMax = now
    now = int(input())
print(nowMax)
'''

'''n = int(input())
if n == 0:
    count = 0
else:
    count = 1
while n != 0:
    n = int(input())
    if n != 0:
        count += 1
print(count)
'''
'''sum = 0
n = 1
while n != 0:
    n = int(input())
    sum += n
print(sum)
'''

1 задача по сумме последовательности

'''countEv = 0
n = 1
while n != 0:
    n = int(input())
    if n % 2 == 0 and n != 0:
        countEv += 1
print(countEv)
'''

''''first = int(input())
i = int(input())
if i > first:
    second,first = first,i
i = int(input())
while (i!=0):
    if i > first:
        second,first=first,i
    elif second<i<first:
        second=i
    i = int(input())
print(second)'''

'''now = int(input())
maxNow = 0
maxPrev = 0
while now != 0:
    if now > maxNow:
        maxPrev = maxNow
        maxNow = now
    elif now > maxPrev:
        maxPrev = now
    now = int(input())
print(maxPrev)'''

2 задача по сумме последовательности

'''now = -1
count = 0
maxNow = 0
while now != 0:
    now = int(input())
    if now > maxNow:
        maxNow = now
        count = 1
    elif now == maxNow:
        count += 1
print(count)'''


5 задача по сумме последовательности

'''prev = -1
count = 0
maxCount = 0
now = int(input())
while now != 0:
    if now == prev:
        count += 1
    else:
        prev = now
        if count >= maxCount:
            maxCount = count
        count = 1
    now = int(input())
if count >= maxCount:
    maxCount = count
print(maxCount)'''

2 задача по сумме последовательности





'''now = int(input())
maxNow = now
maxPrev = now
while now != 0:
    if now >= maxNow and now != 0:
        maxPrev = maxNow
        maxNow = now
    elif maxPrev == maxNow:
        maxPrev = maxNow
    else:
        maxPrev = now
    now = int(input())
print(maxPrev)'''

'''Зато эта работает:
x=-1
first=0
second=0
while x!=0:
x=int(input())
if x>first and x!=0:
second=first
first=x
elif xsecond and x!=0:
second=x
print(second)'''