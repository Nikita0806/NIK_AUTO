def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total

def calculate_rectangle_area(width, height):    # Умножение
    return width * height

def is_prime(number):       # Тестирование функции, которая проверяет, является ли данное число простым
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def find_max(numbers):    # Тестирование функции, которая находит максимальное значение в списке
    if not numbers:
        return None
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value