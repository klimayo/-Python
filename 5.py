revenue = int(input('введите выручку: '))
cost = int(input('введите стоимость издержек: '))

if revenue > cost:
    profit = revenue - cost
    rent = profit/cost
    print(f'отличная работа. У вас {profit} прибыли')
    employee = int(input('Введите количество сотрудников: '))
    profit_1 = profit / employee
    print(profit_1)

elif revenue == cost:
     print("Продолжайте в том же духе")
else:
     print("Необходимо снизить издержки производства")

