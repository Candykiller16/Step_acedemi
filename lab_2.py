# Задание 1
# pos_for_zad_one = [1,2,3,4,5]
# def get_pow():
#     n = int(input())
#     for el in pos_for_zad_one:
#         print(el**n)
#
# get_pow()

# Задание 2
# pos_for_zad_two = [1, 2, 3, 4, 5, 6]
#
#
# def func_two():
#     n = int(input())
#     for el in pos_for_zad_two:
#         if el % n == 0:
#             print(el)
#
#
# func_two()

# Задание 3
# def argmin():
#     pos = [int(i) for i in input().split()]
#     minIndex = pos.index(min(pos))
#     print(minIndex)
#
#
# argmin()

# Задание 4
# pos_for_zad_four = [1,2,3,4,5,6,7]
# list_one = []
# def get_greater():
#     n = int(input())
#     for el in pos_for_zad_four:
#         if el > n:
#             list_one.append(el)
#     print(list_one)
#
# get_greater()
#
# Задание 5

# pos_for_zad_five = [12,2,35,4,56,6,14,88,8]
# a = 5
# b = 25
# list_five = []
# def func_five():
#     for el in pos_for_zad_five:
#         if el in range(a,b+1):
#             list_five.append(el)
#     print(sorted(list_five))
#
# func_five()

# Задание 6
# pos_for_six = [1,2,3,4,5,6,7,8,9,10]
# list_six=[]
# def get_n():
#     n = int(input())
#     pos_six = pos_for_six[1::n]
#     for el in pos_six:
#         list_six.append(el)
#     print(list_six)
#
# get_n()

# Задание 7

# def is_palindrom():
#     n = input()
#     if n == n[::-1]:
#         print('Да, это полиндром')
#     else:
#         print('Нет, это не полиндром')
#
# is_palindrom()
