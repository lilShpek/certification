import csv
import json
import random
import math

# Функция для генерации CSV-файла
def generate_csv_file(file_name, rows):
    with open(file_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['a', 'b', 'c'])  # Заголовок CSV-файла
        for _ in range(rows):
            a, b, c = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)
            csv_writer.writerow([a, b, c])

# Функция для нахождения корней квадратного уравнения
def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2

# Декоратор для сохранения результатов в JSON
def save_to_json(func):
    def wrapper(file_name):
        with open(file_name, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Пропустить заголовок
            data = []
            for row in csv_reader:
                a, b, c = map(int, row)
                roots = func(a, b, c)
                result = {'a': a, 'b': b, 'c': c, 'roots': roots}
                data.append(result)

        with open('results.json', 'w') as json_file:
            json.dump(data, json_file, indent=2)

    return wrapper

# Использование декоратора
@save_to_json
def find_roots_calculate(a, b, c):  # используйте разные имена для декорированной и оригинальной функции
    return find_roots(a, b, c)

# Пример использования
generate_csv_file("input_data.csv", 101)
find_roots_calculate("input_data.csv")

with open("results.json", 'r') as f:
    data = json.load(f)

if 100 <= len(data) <= 1000:
    print(True)
else:
    print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

print(len(data) == 101)


