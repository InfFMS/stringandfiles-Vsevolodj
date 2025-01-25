# Откройте текстовый файл task3.txt для чтения.
# Извлеките все уникальные слова из файла (слова разделяются пробелами и знаками пунктуации).
# Подсчитайте, сколько раз каждое уникальное слово встречается в тексте.
# Запишите результаты в новый файл в формате:
# слово1: количество
# слово2: количество
#
# Убедитесь, что слова записаны в алфавитном порядке.
import string

with open('task3.txt', 'r', encoding='utf-8') as file:
    s=file.read()
    table = str.maketrans("", "", string.punctuation)
    s = s.translate(table)
    s = s.replace('\n', '')
    print(s)
    s=list(map(str, s.split(' ')))
    cesh=dict()
    for elem in s:
        if elem in cesh:
            cesh[elem]+=1
        else:
            cesh[elem]=1
    del cesh['']
    for i in cesh:
        print(f'{i}: {cesh[i]}')
# print(str)
# lst = str.split(" ")
# print(lst)