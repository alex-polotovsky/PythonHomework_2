# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# o	6782 -> 23
# o	0,56 -> 11


def get_summ(number):
    num = str(number)
    summ = 0
    for i in num:
        if i == '.':
            continue
        summ += int(i)
    return summ


def get_summ_2(number):
    num = str(number)
    summ = 0
    for i in num:
        if i.isdigit():
            summ += int(i)
    return summ        


print('Сумма цифр числа: ', get_summ(0.56))
print('Сумма цифр числа: ', get_summ_2(0.56))
