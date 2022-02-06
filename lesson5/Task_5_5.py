# Task 5 Lesson 5

# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


from random import randint

with open("task_5.txt", "w+", encoding="utf-8") as the_file:
    the_file.write(" ".join([str(randint(1, 100)) for _ in range(10)]))
    the_file.seek(0)
    print(sum(map(int, the_file.readline().split())))