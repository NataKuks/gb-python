a = int(input("Введитее результат пробежки к км за 1-ый день: "))
b = int(input("Введите желаемый результат пробежки в км: "))

need_km = a
need_days = 1

while need_km < b:
    a = a + (a * 10 / 100)
    need_days = need_days + 1
    need_km = a
print(f"Вы достигните результата в 3 км на {need_days} день")

