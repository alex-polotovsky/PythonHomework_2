# Задайте список из n чисел последовательности (1+1/n)^n
# и выведите на экран их сумму.


import math

# Вариант 1


def generate_list(n):
    numbers = [math.pow(1+1/i, i) for i in range(1, n+1)]
    return numbers


num = int(input('Enter an integer: '))
print('List "n" numbers: \n', generate_list(num))
print('The sum of the elements: \n', sum(generate_list(num)))
print()

# Вариант 2


def get_list(n):
    numbers = []
    for i in range(1, n+1):
        numbers.append((1+1/i)**i)
    return numbers


print('List "n" numbers: \n', get_list(num))
print('The sum of the elements: \n', sum(get_list(num)))
