# Task 3 Lesson 5

# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

with open("task_3.txt", "r", encoding="utf-8") as emp_salary:
    content = emp_salary.read()
    print(content)

    sal = []
    small_sal = []
    sal_list = content.split('\n')
    print(f"\n {sal_list}")
    for i in sal_list:
        i = i.split()
        if float(i[1]) < 20000:
            small_sal.append(i[0])
        sal.append(i[1])

print(f"\nСписок сотрудников с окладом меньше 20.000 {small_sal}, средняя ЗП {sum(map(float, sal)) / len(sal)}")