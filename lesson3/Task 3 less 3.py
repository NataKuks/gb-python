# Task 3 Less 3

# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
# возвращает сумму наибольших двух аргументов.


def my_func(x, y, z):
    try:
        x = int(x)
        y = int(y)
        z = int(z)
        my_list = [x, y, z]
        my_list.remove(min(my_list))
    except ValueError:
        return "Please,  enter numbers, not string!"
    return f"Amount of 2 largest numbers is: {sum(my_list)}"

print(my_func(input("Enter the 1st number: "), input("Enter the 2nd number: "),
              input("Enter the 3d number: ")))
