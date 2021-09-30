import random


def getSum(a, b):
    return a + b


def convertToNumbers(myList):
    newList = []
    for i in myList:
        newList.append(int(i))
    return newList


def readNumbers(filename):
    with open(filename, 'r') as f:
        data = f.read()

    data = data.strip().split()  # чистим файл и разделяем пробелами, отдает список
    return convertToNumbers(data)


def multiply(List, times=10):
    lst = []
    for i in List:
        lst.append(i * times)
    return lst


def generateInput(filename, minValue, maxValue, lines, count):
    with open(filename, 'w') as f:
        for i in range(lines):
            for j in range(count):
                x = random.randint(minValue, maxValue)
                f.write(str(x))
                f.write(' ')
            f.write('\n')
    return f


def example_1():
    data = readNumbers('files_input1.txt')

    if len(data) > 1:
        res = getSum(data[0], data[1])
        print(res)


def example_2():
    data = readNumbers('files_input1.txt')
    data = multiply(data, 20)
    print(*data)


# generateInput('input1.txt', minValue=1, maxValue=1000, lines=5, count=10)
# min, max, самое частое
generateInput('input2.txt', minValue=1, maxValue=1000, lines=15, count=15)


def readFile(filename):
    myList = []
    with open(filename) as f:
        for line in f:
            line = line.strip().split()  # избавляемся от знака \n и дробим по пробелам
            lst = convertToNumbers(line)
            myList.extend(lst)
    return myList


def example4():
    numbers = readFile('input2.txt')
    print('Мин.значение: ', min(numbers))
    print('Макс.значение: ', max(numbers))


example4()
