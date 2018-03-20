'''a = float(input())
b = float(input())
c = float(input())
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
print('{0:.6f}'.format(s))

n = int(input())
i = 1
s = 0
while i <= n:
    s += 1 / i ** 2
    i += 1
print('{0:.6}'.format(s))

x = float(input())
x = x - int(x)
print('{0:.6f}'.format(x))

x = float(input())
rub = int(x)
cop = round((x - int(x)) * 100)
print(rub, cop)

import math
x = float(input())
epsilon = 5 * 10**-10
if x - int(x) < 0.5 - epsilon:
    print(math.floor(x))
else:
    print(math.ceil(x))

p = int(input())
x = int(input())
y = int(input())
xCop = 100 * x + y
xCopNew = xCop + xCop * p / 100
xNew = int(xCopNew / 100)
yNew = int(xCopNew - xNew * 100)
print(xNew, yNew)

p = int(input())
x = int(input())
y = int(input())
k = int(input())
i = 1
while i <= k:
    xCop = 100 * x + y
    xCopNew = xCop + xCop * p / 100
    x = int(xCopNew / 100)
    y = int(xCopNew - x * 100)
    i += 1
print(x, y)


2 задача по округлению вещественных чисел

import math
a = float(input())
b = float(input())
c = float(input())
d = b ** 2 - 4 * a * c
if d == 0:
    x0 = -b /(2 * a)
    print('{0:.6f}'.format(x0))
if d > 0:
    x1 = (-b - math.sqrt(d)) /(2 * a)
    x2 = (-b + math.sqrt(d)) /(2 * a)
    if x1 > x2:
        x1, x2 = x2, x2
    print('{0:.6f}'.format(x1), '{0:.6f}'.format(x2))

1 задачи по округлению вещественных чисел


a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
if a == 0 and (c != 0 and b != 0):
    y = e / b
    x = (f * b - d * e) / (c * b)
elif b == 0 and (a != 0 and d != 0):
    x = e / a
    y = (f * a - c * e) / (a * d)
elif c == 0 and (a != 0 and d != 0):
    x = (e * d - b * f) / (a * d)
    y = f / d
elif d == 0 and (c != 0 and e != 0):
    x = f / c
    y = (e * d - b * f) / (e * d)
else:
    y = (f - c * e / a) / (d - b * c / a)
    x = (e - b * y) / a
print('{0:.6f}'.format(x), '{0:.6f}'.format(y))


1 задача по округлению вещественных чисел

s = input()
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])
print(len(s))

string = input()
pos1 = string.find('f')
if pos1 != -1:
    print(pos1, end=' ')
    pos2 = string.rfind('f', pos1 + 1)
    if pos2 != -1:
        print(pos2)

string = input()
pos1 = string.find('h')
pos2 = string.rfind('h', pos1+1)
string1 = string[:pos1]
string2 = string[pos2+1:]
print(string1 + string2)

1 задача по find

string = input()
pos = string.find('f')
substring = string[pos + 1:]
if pos == -1:
    print(-2)
elif substring.find('f') != -1:
    print(substring.find('f') + len(string[:pos+1]))
else:
    print(-1)

string = input()
pos = string.find(' ')
substring1 = string[:pos]
substring2 = string[pos + 1:]
print(substring2 + ' ' + substring1)

string = input()
print(string.count(' ') + 1)

string = input()
print(string.replace('1', 'one'))


string = input()
print(string.replace('@', ''))

3 задачи на replace
'''
