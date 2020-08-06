a = float(input('введите количество км '))
b = float(input('введите общее количество км '))

day = 1

if a > b:
    print(day)
while a < b:
    a = a + a / 10
    day += 1
print(day)