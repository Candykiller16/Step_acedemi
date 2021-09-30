d = {}
d1 = {'Ivanov': 27, 'Petrov': 39, 'Sidorov': 27}
print(d1)
print(d1['Petrov'])
print(d1['Ivanov'])
print(d1['Sidorov'])
if 'Ivanova' in d1:
    print(d1['Ivanova'])

print(d1.get('Ivanova')) # достать элемент по ключу
d1['Ivanov'] = 25
d1['Petrov'] = 38
d1['Ivanova'] = 18
print(d1)

for k, v in d1.items(): # чтобы пройти по ключам и значениям пиши items
    print(k, ' -> ', v)

for k in d1: # отдаёт только ключи
    print(k)

print(d1.items())
print(d1.keys()) # отдаст только ключи
print(d1.values()) # отдаст только значения
print(d1.items()) # отдаст ключ: значение
d1['Ivanovava'] = 16 # чтобы добавить ключ значение
d1.pop('Ivanovava') # чтобы убрать одну пару
del d1['Ivanova'] # также чтобы удалить
d1.clear() # очистить весь словарь

