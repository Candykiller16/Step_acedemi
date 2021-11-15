import os
from chardet import detect

# get file encoding type
def get_encoding_type(file):
    with open(file, 'rb') as f:
        rawdata = f.read()
    return detect(rawdata)['encoding']

print(get_encoding_type('Lopatin_dictionary.txt'))

with open('Lopatin_dictionary.txt', 'r', encoding='windows-1251') as d:
    with open('Dictionaty', 'w') as w:
        for i in d:
            i.encode("utf-8")
            w.write(i)





