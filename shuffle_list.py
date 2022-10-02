# Реализуйте алгоритм перемешивания списка.


from random import randint, shuffle


numbers = [1, 2, 3, 4]

# Вариант 1.

shuffle(numbers)
print(numbers)

# Вариант 2. 

for i in range(len(numbers)):
    j = randint(0, len(numbers)-1)
    temp = numbers[i]
    numbers[i] = numbers[j]
    numbers[j] = temp
    
print(numbers)
