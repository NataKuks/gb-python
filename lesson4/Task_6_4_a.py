# Task 6 less 4

# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля i tertools. Обратите внимание, что
# создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.

# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10
# завершаем цикл. Во втором также необходимо предусмотреть условие, при котором
# повторение элементов списка будет прекращено.

# -------------- a) ----------------

from sys import argv
from itertools import count

name_, start_from, end_with = argv

print("Файл вычисления: ", name_)
print("Начать с числа: ", start_from)
print("Закончить числом: ", end_with)


def make_nums ():
    global name_, start_from, end_with
    start_from = int(start_from)
    end_with = int(end_with)
    el = 0
    for el in count(start_from):
        if el > end_with:
            break
        else:
            print(el)
            #return

make_nums()
