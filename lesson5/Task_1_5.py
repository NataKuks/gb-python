# Task 1 less 5

# Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.


my_file = open("task_1.txt", "w", encoding="utf-8")
new_string = input("Введите текст:\n")

while new_string:
    my_file.write(new_string)
    new_string = input("Введите текст:\n")
    my_file.write(" ")
    if not new_string:
        break

my_file.close()

with open("task_1.txt", "r", encoding="utf-8") as my_file:
    content = my_file.read()
    print(content)
    print(type(content))
