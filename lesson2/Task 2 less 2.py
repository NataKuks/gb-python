# Task 2 Less 2
# Для списка реализовать обмен значений соседних элементов,
# т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном кол-ве эл-тов последний сохранить на своем месте.
# Для заполнения списка эл-тов необходимо использовать функцию input().



my_list = list(input("Введите любое количество чисел, не используя пробел: "))
print(my_list)

for el in range(1, int(len(my_list)), 2):
    my_list[el], my_list[el - 1] = my_list[el - 1], my_list[el]

print(my_list)
