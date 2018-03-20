'''def merge(a, b):
    i = 0
    j = 0
    c = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    while i < len(a):
        c.append(a[i])
        i += 1
    while j < len(b):
        c.append(b[j])
        j += 1
    return c


a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*merge(a, b))


1 задача

int(input())
listN = list(map(int, input().split()))
listN.sort()
print(*listN)


1 задача на сортировку

dataN = tuple(map(int, input().split()))
data = dataN[0]
n = dataN[1]
listD = []
for i in range(n):
    listD.append(int(input()))
listD.sort()
sum = 0
k = 0
for i in range(n):
    sum += listD[i]
    if sum > data:
        break
    k += 1
print(k)

n = int(input())
listT = list(map(int, input().split()))
m = int(input())
listV = list(map(int, input().split()))
listTN = []
listVN = []
for i in range(n):
    tupleT = listT[i], (i + 1)
    listTN.append(tupleT)
listTN.sort()
for i in range(m):
    tupleV = listV[i], (i + 1)
    listVN.append(tupleV)
listVN.sort()
listRes = []
start = 0
for i in range(n):
    min = 10 ** 10
    numV = 0
    for j in range(start, m):
        breakflag = False
        distans = abs(listTN[i][0] - listVN[j][0])
        if distans < min:
            numV = j
            min = distans
        else:
            breakflag = True
            listRes.append((listTN[i][1], listVN[j-1][1]))
            break
    if not breakflag:
        listRes.append((listTN[i][1], listVN[j][1]))
    start = numV
listRes.sort()
for i in range(n):
    listRes[i] = listRes[i][1]
print(*listRes)


1 задача по чтению до конца вввода

fileI = open('input.txt', 'r', encoding='utf8')
listM = []
for line in fileI:
    temp = list(map(str, line.split()))
    temp = [temp[0], temp[1], temp[3]]
    listM.append(temp)
listM.sort()
fileO = open('output.txt', 'w', encoding='utf8')
for i in listM:
    print(*i, file=fileO)
fileI.close()
fileO.close()


def CountSort(a):
    listN = [0] * 101
    for i in a:
        listN[i] += 1
    for now in range(101):
        print((str(now) + ' ') * listN[now], end='')


listP = list(map(int, input().split()))
CountSort(listP)


2 задачи на сортировку подсчетом

n = int(input())
listR = []
for i in range(n):
    temp = input().split()
    tupleO = (temp[0], int(temp[1]))
    listR.append(tupleO)
listR.sort(key=lambda x: x[1], reverse=True)
for i in range(n):
    print(str(listR[i][0]))

1 задача на сортировку подсчетом

fileIn = open('input.txt', 'r', encoding='utf8')
lines = fileIn.readlines()
k = int(lines[0])
sumList = []
for i in range(1, len(lines)):
    tempList = list(map(str, lines[i].split()))
    s1 = int(tempList[-1])
    s2 = int(tempList[-2])
    s3 = int(tempList[-3])
    if s1 >= 40 and s2 >= 40 and s3 >= 40:
        sum = s1 + s2 + s3
        sumList.append(sum)
sumList.sort(reverse=True)
n = len(sumList)
if n <= k:
    res = 0
else:
    if sumList[0] == sumList[k]:
        res = 1
    else:
        for i in range(k, 0, -1):
            if sumList[i] < sumList[i - 1]:
                res = sumList[i - 1]
                break
fileOu = open('output.txt', 'w', encoding='utf8')
print(res, file=fileOu)
fileIn.close()
fileOu.close()



'''
'''
почему не работает?

int(input())
listN = list(map(int, input().split()))
# listN.sort()
# print(*listN)
print(*listN.sort())
'''
#            listRes.append((listTN[i][1], listVN[j][1]))


tempList = list(map(int, lines[i].split()))
n = int(input())
listT = list(map(int, input().split()))
m = int(input())
listV = list(map(int, input().split()))
listTN = []
listVN = []
for i in range(n):
    tupleT = [listT[i], (i + 1)]
    listTN.append(tupleT)
listTN.sort()
print(*listTN)
for i in range(m):
    tupleV = [listV[i], (i + 1)]
    listVN.append(tupleV)
listVN.sort()
print(*listTN)
listRes = []
start = 0
for i in range(n):
    min = 10 ** 10
    numV = 0
    for j in range(start, m):
        distans = abs(listTN[i][0] - listVN[j][0])
        if distans < min:
            numV = j
            min = distans
            listTN[i][2] = listVN[j][1]
        else:
            break
    start = numV
# listRes.sort()
#print(*listRes)
print(*listTN)

if abs(listTN[i][0] - listVN[j][0]) < abs(listTN[i][0] - listVN[j - 1][0]):
    listRes.pop(i - 1)
else:

    n = int(input())
    listT = list(map(int, input().split()))
    m = int(input())
    listV = list(map(int, input().split()))
    listTN = []
    listVN = []
    for i in range(n):
        tupleT = listT[i], (i + 1)
        listTN.append(tupleT)
    listTN.sort()
    # получили отсортированный список из кортежей расстояние от нулевой точки до города i - порядковый номер города + 1
    # print(*listTN)
    for i in range(m):
        tupleV = listV[i], (i + 1)
        listVN.append(tupleV)
    listVN.sort()
    # получили отсортированный список из кортежей расстояние от нулевой точки до убежища i - порядковый номер убежища + 1
    # print(*listVN)
    listRes = []
    # список для хранения результат из кортежей порядковый номер города - порядковый номер ближайшего убежища
    start = 0
    # переменная для начала вложенного цикла
    for i in range(n):
        min = 10 ** 10
        numV = 0
        # переменная с номером нужного убежища
        for j in range(start, m):
            breakflag = False
            distans = abs(listTN[i][0] - listVN[j][0])
            # модуль разности расстояний от нулевой точки для города и убежища
            if distans < min:
                numV = j
                min = distans
            # обновляем минимум расстояния
            else:
                breakflag = True
                listRes.append((listTN[i][1], listVN[j - 1][1]))
                break

        if not breakflag:
            listRes.append((listTN[i][1], listVN[j][1]))
        # обновляем начало для вложеного цикла
        start = numV
    listRes.sort()
    print(*listRes)


n = int(input())
listT = list(map(int, input().split()))
m = int(input())
listV = list(map(int, input().split()))
listTN = []
listVN = []
for i in range(n):
    tupleT = listT[i], (i + 1)
    listTN.append(tupleT)
listTN.sort()
# получили отсортированный список из кортежей расстояние от нулевой точки до города i - порядковый номер города + 1
# print(*listTN)
for i in range(m):
    tupleV = listV[i], (i + 1)
    listVN.append(tupleV)
listVN.sort()
# получили отсортированный список из кортежей расстояние от нулевой точки до убежища i - порядковый номер убежища + 1
# print(*listVN)
listRes = []
# список для хранения результат из кортежей порядковый номер города - порядковый номер ближайшего убежища
start = 0
# переменная для начала вложенного цикла
for i in range(n):
    min = 10 ** 10
    numV = 0
# переменная с номером нужного убежища
    for j in range(start, m):
        breakflag = False
        distans = abs(listTN[i][0] - listVN[j][0])
# модуль разности расстояний от нулевой точки для города и убежища
        if distans < min:
            numV = j
            min = distans
# обновляем минимум расстояния
        else:
            breakflag = True
            listRes.append((listTN[i][1], listVN[j-1][1]))
            break

    if not breakflag:
        listRes.append((listTN[i][1], listVN[j][1]))
# обновляем начало для вложеного цикла
    start = numV
listRes.sort()
for i in range(n):
    listRes[i] = listRes[i][1]
print(*listRes)



n = len(sumList)
if n < k:
    res = 0
elif n = k:
    res = 1
for i in range(k, 0, -1):
    if sumList[i] <= sumList[i - 1]:
        res = sumList[i - 1]
        break