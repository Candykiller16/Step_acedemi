def getNumbers():
    rawData = input().split()
    data = []
    for v in rawData:
        data.append(int(v))
    return data


def pretty_print(myList):
    for elem in myList:
        print(elem, end=' ')


def getGreater():
    data = getNumbers()

    if len(data) < 2:
        return

    res = []
    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            res.append(data[i])

    pretty_print(res)


def getPairWithSameSign():
    data = getNumbers()

    if len(data) < 2:
        return

    res = []
    for i in range(1, len(data)):
        if (data[i] > 0 and data[i - 1] > 0) or (data[i] < 0 and data[i - 1] < 0):
            res.append(data[i - 1])
            res.append(data[i])
        if res:
            break

    pretty_print(res)


def findMaxElem():
    data = getNumbers()

    maxValue = max(data)
    idx = data.index(maxValue)
    print(maxValue, idx)


def swapElems():
    data = getNumbers()

    maxIdx = data.index(max(data))
    minIdx = data.index(min(data))
    maxValue = data[maxIdx]
    minValue = data[minIdx]
    data[maxIdx] = minValue
    data[minValue] = maxValue

    pretty_print(data)


def removeElem1():
    data = getNumbers()

    idx = int(input())
    data.pop(idx)

    pretty_print(data)


def removeElem2():
    data = getNumbers()

    idx = int(input())

    l = len(data)
    for i in range(idx, l - 1):
        data[i] = data[i + 1]
    data.pop()

    pretty_print(data)


def removeElem3():
    data = getNumbers()

    idx = int(input())

    data = data[:idx] + data[idx + 1:]

    pretty_print(data)


findMaxElem()
