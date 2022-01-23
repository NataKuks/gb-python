#Task 4 less 3

# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать
# в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной
# функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с
# помощью оператора **. Второй — более сложная реализация без оператора **,
# предусматривающая использование цикла.

def my_func(x, y):
    try:
        x = int(x)
        y = int(y)
        result = 1 / (x ** abs(y)) #стоит ли предусмотреть исключение (и как?), если пользователь будет вводить положительный y?
        #в принципе можно использовать условие только x ** y и прога все считает корректно
    except ZeroDivisionError:
        return "Your first number cannot be Zero"
    except ValueError:
        return "Please, enter NUMBERS only according to conditions of the task."
    return round(result, 4)

print(my_func(input("Enter real positive number: "), input("Enter negative number: ")))

