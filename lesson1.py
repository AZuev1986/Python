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
