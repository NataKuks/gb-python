# Task 2 less 3

# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о
# пользователе одной строкой.


def pers_data(name, surname, birth_year, city, email, tel):
    return f"Name - {name}, Surname - {surname}, birth year - {birth_year}, city - {city}, e-mail - {email}, " \
           f"telephone number - {tel}"

print(pers_data(name = input("Enter your name: "), surname = input("Enter your surname: "), #почему подчеркивает волной? что не нра?
                birth_year = input("Enter year of your birth: "), city = input("Enter your city: "),
                email = input("Enter your e-mail: "), tel = input("Enter your tel number: ")))

