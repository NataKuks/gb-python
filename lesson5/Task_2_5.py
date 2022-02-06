# Task 2 Lesson 5

# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке.


with open("task_2.txt", "r", encoding="utf-8") as poem:
    content = poem.read()
    print(content)

with open("task_2.txt", "r", encoding="utf-8") as poem:
    content = poem.readlines()
    #print(type(content))
    print(f"Количество строк в файле: {len(content)}\n")

with open("task_2.txt", "r", encoding="utf-8") as poem:
    content = poem.readlines()
    for index, value in enumerate(content, 1):
        number_of_words = len(value.split())
        print(f"Строка {index} содержит {number_of_words} слов(-а)")








