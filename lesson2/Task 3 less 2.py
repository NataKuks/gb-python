#Task 3 Lesson 2
#Пользователь вводит месяц в виде целого числа от 1 до 12.
#Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
#Напишите решения через list и dict.

seasons_names = ["зима", "весна", "лето", "осень"]
seasons_dict = {1: "зима", 2: "весна", 3: "лето", 4: "осень"}

month = int(input("Введите месяц года по его номеру: "))

if month == 1 or month == 2 or month == 12:
     print(f"Месяц с кодом {month} относится к поре года '{seasons_names[0]}'")
     print(f"Месяц с кодом {month} относится к поре года '{seasons_dict.get(1)}'")
elif month == 3 or month == 4 or month == 5:
    print(f"Месяц с кодом {month} относится к поре года '{seasons_names[1]}'")
    print(f"Месяц с кодом {month} относится к поре года '{seasons_dict.get(2)}'")
elif month == 6 or month == 7 or month == 8:
    print(f"Месяц с кодом {month} относится к поре года '{seasons_names[2]}'")
    print(f"Месяц с кодом {month} относится к поре года '{seasons_dict.get(3)}'")
elif month == 9 or month == 10 or month == 11:
    print(f"Месяц с кодом {month} относится к поре года '{seasons_names[3]}'")
    print(f"Месяц с кодом {month} относится к поре года '{seasons_dict.get(4)}'")
else:
     print(f"Месяца с кодом {month} не существует.")



