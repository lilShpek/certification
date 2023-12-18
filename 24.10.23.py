# def factorial(n):
#     number = 1
#     for i in range(1, n + 1):
#         number *= i
#         yield number
#         print(f"Генерирую число {number}")

# f = iter(factorial(5))
# print(next(f))
# print(next(f))
# print(next(f))

# print()
# print(*iter(factorial(5)))

# for item in factorial(5):
#     print(f"{item =}")

# for fact in factorial(5):
#     pass


# Задание №1
# ✔ Пользователь вводит строку из четырёх
# или более целых чисел, разделённых символом “/”.
# Сформируйте словарь, где:
# ✔второе и третье число являются ключами.
# ✔первое число является значением для первого ключа.
# ✔четвертое и все возможные последующие числа
#  хранятся в кортеже как значения второго ключа.

# list_user = input("Введите строку: ")
# key_1, key_2, key_3, *key_4 = list_user.split('/')

# result = {key_2: key_1,
#           key_3: tuple(key_4)}

# print(result)


# Задание №2
# ✔ Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку.

# list_user = "Привет мир"
# print({i: ord(i) for i in set(list_user) })


# Задание №3
# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю

# list_user = "Привет мир"
# result = iter({i: ord(i) for i in set(list_user)}.items())
# for i in range(5):
#     print(next(result))


# Задание №4
# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите
# числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку

# even_numbers = (x for x in range(101) if x % 2 == 0 and sum(map(int, str(x))) != 8)

# for num in even_numbers:
#     print(num)


# Задание №5
# ✔ Напишите программу, которая выводит
# на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.

# result = ('Fizz' * (x % 3 == 0) + 'Buzz' * (x % 5 == 0) 
#           or x for x in range(1, 101))
# сначала слева пытаемся сформировать строку 
# из физза или базза или вместе
# затем выбираем через or 
# либо сформированную строку либо само число
# и если строку сформировать не удалось, то есть в итоге False
# то автоматом распечатается правая часть or
# то есть само число х
# а если же строку сформировать удалось, то печатаем именно ее


# Задание №6
# ✔ Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного
# генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт»
# без перехода на новую строку.

# def gen():
#     for i in (2, 6):
#         for j in range(2, 11):
#             for k in range(i, i + 4):
#                 yield f'{k} x {j:<2} = {k * j:<2} \t\t'
#             print()
#         print()


# for string in gen():
#     print(string, end='')


# №7
# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».


# def is_prime(number):
#     if number <= 1:
#         return False
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             return False
#     return True

# def generate_primes(N):
#     count = 0
#     current_number = 2

#     while count < N:
#         if is_prime(current_number):
#             yield current_number
#             count += 1
#         current_number += 1

# # Использование функции-генератора для получения первых N простых чисел
# N = 10  # Замените на количество простых чисел, которое вам нужно
# for prime in generate_primes(N):
#     print(prime)



# import os
# def get_file_info(file_path):
#     file_dir, file_name = os.file_path.split(file_path)
#     name, extention = os.file_path.split(file_name)
#     return file_dir, name, extention

# file_path = "C:/Users/User/Documents/example.txt"
# result = get_file_info(file_path)
# print(result)