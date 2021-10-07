from collections import Counter

def readFile(filename):
    listt = []
    with open(filename, 'r') as f:
        for i in f:
            listt.append(int(i))
    return listt


readFile('input.txt')

def one():
    dict_for_def = {}
    count_for_dict = 1
    list_unical_one = []
    list_unical_two = []
    count = 1
    listOne = readFile('input.txt')
    sumList = sum(listOne)
    minList = min(listOne)
    maxList = max(listOne)
    for i in listOne:
        if i not in listOne:
            list_unical_one.append(i)
            count +=1
    # count_unical_numbers = len(list_unical_one)
    count_unical_numbers = len(set(listOne))
    c = Counter(listOne)

    for j in listOne:
        if j not in dict_for_def:
            dict_for_def[j] = 0
        dict_for_def[j] += 1

    result_string = ''
    for k, v in c.items():
        result_string += str(k) + '\t' + str(v) + '\n'

    with open('result.txt', 'w') as f:

        # f.write('Сумма всех чисел в списке ' + str(sumList) + '\n')
        # f.write('Максимальное = ' + str(maxList) + ' и минимальное = ' + str(minList) + ' числа в списке' + '\n')
        # f.write('Cколько всего уникальных чисел содержится в списке -> ' + str(count_unical_numbers) + '\n')
        f.write(result_string)

one()

s = '''
     ╓──╗
'''



