# Откройте текстовый файл task2.txt для чтения.
# Считайте его содержимое в строку.
# Найдите и замените все вхождения слова "Python" на слово "Питон" (регистр учитывать).
# Запишите обновленный текст в новый файл с другим именем.
# Выведите на экран сообщение о количестве произведённых замен.
with open('task4.txt', encoding='utf-8') as f:
    str = f.read()
lst = str.split(' ')
n = 0
for i in range(0,len(lst)):
    if lst[i]=="Python":
        lst[i]="Питон"
        n +=1
    if lst[i]=="\nPython":
        lst[i]="\nПитон"
        n +=1
print(n)
lst = " ".join(lst)
with open('task2.1.txt', 'w') as f:
    for s in [lst]:
        f.write(s)
print(lst)

