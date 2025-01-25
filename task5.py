# Откройте текстовый файл task5.txt для чтения.
# Найдите самое длинное слово в тексте. Если таких слов несколько, выберите первое из них.
# Запишите это слово и его длину в новый файл в формате:
# Самое длинное слово: слово
# Его длина: длина
#
# Выведите это слово и длину в консоль.
import string
with open('task5.txt', 'r', encoding='utf-8') as file:
    s=file.read()
    table = s.maketrans("", "", string.punctuation)
    s = s.translate(table)
    s = list(map(str, s.split(' ')))
    line=0
    st=''
    for i in s:
        if len(i)>line:
            line=len(i)
            st=i
    print('Самое длинное слово:', st)
    print('Его длина:', line)
with open('task5_1.txt', 'w', encoding='utf-8') as f:
    f.write(f'Самое длинное слово: {st}\n Его длина: {line}')