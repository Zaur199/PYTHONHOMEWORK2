# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для получения случайного int
import random
lst = [5, 8, -9, 4, -1, 0, 3]
print(f'Текущий список {lst}')

for i in range(len(lst) - 1):
    j = random.randint(0, i + 1)
    lst[i], lst[j] = lst[j], lst[i]
print(f'Перемещанный список {lst}')