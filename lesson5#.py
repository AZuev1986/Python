'''
a = int(input())
b = int(input())
for i in range(a, b + 1):
    print(i, end=' ')


a = int(input())
b = int(input())
if a < b:
    for i in range(a, b + 1):
        print(i, end=' ')
else:
    for i in range(a, b - 1, -1):
        print(i, end=' ')


2 задача на  кортежи

n = int(input())
print('+___ ' * n, sep=' ')
for i in range(1, n + 1):
    print('|' + str(i) + ' /', end=' ')
print()
print('|__\\ ' * n, sep=' ')
print('|    ' * n, sep=' ')


1 задача на  кортежи

n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='', sep='')
    print()

5 задач на кортежи


print(' '.join(input().split()[::2]))


# комментарий
numList = list(map(int, input().split()))
s = str()
for n in numList:
    if n % 2 == 0:
        s += str(n) + ' '
print(s)


numList = list(map(int, input().split()))
s = 0
for n in numList:
    if n > 0:
        s += 1
print(s)

numList = list(map(int, input().split()))
max = numList[0]
indexMax = 0
for i in range(0, len(numList)):
    if numList[i] >= max:
        max = numList[i]
        indexMax = i
print(max, indexMax)


numList = list(map(int, input().split()))
prev = numList[0]
s = str()
for i in range(1, len(numList)):
    if numList[i] > prev:
        s += str(numList[i]) + ' '
    prev = numList[i]
print(s)

4 задачи на split и join

numList = list(map(int, input().split()))
minP = 1000
for i in range(0, len(numList)):
    if numList[i] > 0:
        minP = min(numList[i], minP)
print(minP)


3 задачи на split и join


2 задачи на методы списков


n = int(input())
numList = list(map(int, input().split()))
x = int(input())
minD = 2001
minDN = numList[0]
for i in range(len(numList)):
    if abs(x - numList[i]) < minD:
        minD = abs(x - numList[i])
        minDN = numList[i]
print(minDN)


2 задачи на обработку списков

numList = list(map(int, input().split()))
for i in range(1, len(numList), 2):
    numList[i - 1], numList[i] = numList[i], numList[i - 1]
print(' '.join(map(str, numList)))

1 задача на обработку списков

numList = list(map(int, input().split()))
minL = numList[0]
maxL = numList[0]
for i in numList:
    if i < minL:
        minL = i
    if i > maxL:
        maxL = i
ind1 = numList.index(maxL)
ind2 = numList.index(minL)
numList[ind1] = minL
numList[ind2] = maxL
print(*numList)



'''
'''
почему не работает?
numList = list(map(int, input().split()))
a = list()
for i in range(0, len(numList), 2):
    a = a + numList[i]
print(' '.join(map(str, a)))


почему не работает?
numList = list(map(int, input().split()))
a = []
for i in (1, len(numList)):
    if numList[i] % 2 == 0:
        a = a + list(numList[i])
print(' '.join(map(str, a)))


почему не работает?
numList = list(map(int, input().split()))
s = str()
for n in numList:
    if n % 2 == 0:
        s += ' '.join(str(n))
print(s)
'''
numList = list(map(int, input().split()))
s = str()
for n in numList:
    if n % 2 == 0:
        s += ' '.join(str(n))
print(s)

print(' '.join([str(x) for x in map(int, input().split()) if x % 2 == 0]))