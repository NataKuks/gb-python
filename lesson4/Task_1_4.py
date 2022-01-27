from sys import argv

task_name, hours, rate, bonus = argv

print(argv)
print("Расчет ЗП: ", task_name)
print("Количество отработанных часов: ", hours)
print("Ставка: ", rate)
print("Сумма бонусов: ", bonus)

def salary_calc():
    try:
        global hours, rate, bonus
        hours = float(hours)
        rate = float(rate)
        bonus = float(bonus)
        salary_res = (hours * rate) + bonus
    except ValueError:
        return "Введите числовые данные!"
    return f"Заработная плата сотрудника составила: {salary_res}"

print(salary_calc())


