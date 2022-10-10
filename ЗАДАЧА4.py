# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.


with open ('file.txt', 'r') as my_file:
    data = my_file.read()
    lst = data.split()
    res = int(lst[0])*int(lst[1])*int(lst[2])*int(lst[3])*int(lst[4])*int(lst[5])*int(lst[6])*int(lst[7])
    print(lst)
    print(f'Произведение элементов на указанных позициях равна:{res}')