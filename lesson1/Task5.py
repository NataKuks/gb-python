revenue = int(input("Введите сумму выручки за период: "))
cost = int(input("Введите сумму затрат за период: "))
employees = int(input("Введите численность вашей компании: "))

profit = 0
loss = 0

if revenue > cost:
    profit = revenue - cost
    print("Прибыль составила: ", profit)
    profitability = (profit / revenue) * 100
    print(f"Рентабельность составила: {profitability} %")
    prof_emp = profit / employees
    print("Прибыль в расчете на 1-го сотркдника за период составила: ", prof_emp)
else:
    loss = cost - revenue
    print(f"Вы не заработали в этом периоде. Ваши убытки составили: {loss}. Расчет прибыли на 1-го сотрудника не произведен.")


