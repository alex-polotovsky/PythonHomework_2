# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.


from random import randint, sample


def get_list(n):
    """Принимает число и возвращает список на его основе"""
    return list(range(-n, n+1))


def get_position(input_list):
    """Принимает список и возвращает случайно выбранные позиции.
    Реализация 1.
    """
    count = randint(1, len(input_list))
    print('Count: ', count)
    indices = range(len(input_list))
    result = sample(indices, count)
    return result


def get_position_2(input_list):
    """Принимает список и возвращает случайно выбранные позиции.
    Реализация 2.
    """
    count = randint(1, len(input_list))
    print('Count: ', count)
    indices = set()
    while len(indices) < count:
        indices.add(randint(0, len(input_list)-1))
    return indices


def create_file(collection, path):
    """Принимает коллекцию и  путь к файлу 
    и построчно записывает коллекцию в файл.
    """
    with open(path, 'w') as f:
        for i in collection:
            f.write(f'{i}\n')


def get_product(input_list, path):
    """Принимает список и путь к файлу и
    возвращает произведение элементов с выбранных позиций
    """
    prd = 1
    with open(path, 'r') as f:
        for line in f:
            output = input_list[int(line)]
            print(output, end=', ')
            prd *= output 
    return prd


my_list = get_list(6)
print('Input list: ', my_list)

index_list = get_position_2(my_list)
print('Positioin collection: ', index_list)

create_file(index_list, 'file.txt')

product = get_product(my_list, 'file.txt')
print('Product: ', product)
