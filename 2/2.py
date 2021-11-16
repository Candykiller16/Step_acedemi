import re
import os
from chardet import detect

# get file encoding type
def get_encoding_type(file):
    with open(file, 'rb') as f:
        rawdata = f.read()
    return detect(rawdata)['encoding']

print(get_encoding_type('Lopatin_dictionary.txt')) # windows-1251

with open('Lopatin_dictionary.txt', 'r', encoding='utf-8') as d:
    with open('Dictionaty.txt', 'w') as w:
        for i in d:
            i.encode("utf-8")
            w.write(i)

def set_dict():
    with open('Dictionary1.txt', 'r') as d:
        a = []
        for i in d:
            a.append(i.replace('\n', ''))
        return set(a)

def find_fords_with_len(length):
    d = set_dict()
    with open('File_for_len_words.txt', 'w', encoding='utf-8') as file:
        for i in d:
            if len(i) == length:
                file.write(i + '\n')

def fist_letter_words(letter):
    d = set_dict()
    with open('First_letter_file.txt', 'w', encoding='utf-8') as file:
        for i in d:
            if i[0] == letter:
                file.write(i + '\n')


def find_by_mask():
    with open('Dictionary.txt', 'r',encoding="utf-8") as d:
        for i in d:
            result = re.findall(r'ультра\w+',i)
            if result!=[]:
                print(result)

find_fords_with_len(8)
fist_letter_words('б')
find_by_mask()



