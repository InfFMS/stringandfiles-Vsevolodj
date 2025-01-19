# Откройте текстовый файл для чтения task1.txt.
# Подсчитайте:
# Общее количество строк в файле.
# Общее количество слов во всем тексте файла.
# Общее количество символов (включая пробелы).
# Выведите полученную статистику на экран.
with open('task1.txt', encoding="utf-8") as f:
    str = f.read()
amount = 1 # так как строк на 1 больше чем \n, их считает эта переменная
for i in range (0,len(str)):
    if str[i] == "\n":
        amount+=1
print("Количесво строк:", amount)
amount_spase = 0
for i in range (0,len(str)):
    if str[i] == " " and str[i-1] != "—" and str[i-1] != "." and str[i-1] != " " or str[i] == ".":
        amount_spase+=1
print("Количесво слов:", amount_spase)

print("Количесво символов:", len(str))