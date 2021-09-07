from random import randint
listt = []
for i in range(20):
    n = randint(1, 100)
    listt.append(n)


def minimum():
    minun = min(listt)
    print(minun)

def maximum():
    maxu = max(listt)
    print(maxu)

def summa():
    suma = sum(listt)
    print(suma)


def MinMaxSum():
    maxElem, maxIdx = listt[0], 0
    minElem, minIdx = listt[0], 0
    sumElem = 0
    print(listt)
    for ind, val in enumerate(listt):
        sumElem += val
        if val > maxElem :
            maxElem = val
            maxIdx = ind
        elif val < minElem:
            minElem = val
            minIdx = ind

    print(maxElem, maxIdx, minElem, minElem,  minIdx, sumElem, sep='__')
    print()
    m = listt.index(maxElem)
    n = listt.index(minElem)
    listt[m], listt[n] = listt[n], listt[m]
    print(listt)
    #
    # m = listt.index(m)
    # n = listt.index(n)
    # listt[m], listt[n] = listt[n], listt[m]

MinMaxSum()