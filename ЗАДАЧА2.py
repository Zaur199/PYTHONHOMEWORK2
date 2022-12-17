#Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, а так же сумму элементов списка.
#Пример:
#Для n=4 -> [2, 2.25, 2.37, 2.44]
#Сумма 9.06
n = int(input("Введите число: "))
lst = []
sum = 0
x = 0
for i in range(1, n + 1):
    x = round((1 + 1/i)**i, 2)
    lst.append(x)
    sum = round(sum + (1 + 1/i)**i, 2)
print(f'Для n = {n} -> {lst}')
print(f'Сумма равна: {sum}')