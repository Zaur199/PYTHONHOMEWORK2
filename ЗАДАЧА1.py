# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def NumberSum(item):
    result = 0
    i = 0
    for i in item:
        if (i != '.') and (i != '-'):
            result = result + int(i)
    return result

num = float(input('Введите вещественное число: '))
item = str(num)
print(f'Сумма:{NumberSum(item)}')
