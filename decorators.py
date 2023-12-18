# Задание №1
# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.


from typing import Callable
from random import randint

# Задание №1
# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.

def guess_num(rnd_num: int, turns: int) -> Callable:
    def wrapper():
        for _ in range(turns):
            user_num = int(input("Введите число "))
            if user_num == rnd_num:
                print("Ура, вы угадали!")
                return 
            print("Вы не угадали")
    return wrapper

def guess_num2(turns: int) -> Callable:
    def wrapper(rnd_num: int):
        for _ in range(turns):
            user_num = int(input("Введите число "))
            if user_num == rnd_num:
                print("Ура, вы угадали!")
                return 
            print("Вы не угадали")
    return wrapper

# guess_num(5,3)()





# Задание №2
# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# из диапазонов.


# def guess_num(rnd_num: int, turns: int) -> Callable:
#     def wrapper():
#         for _ in range(turns):
#             user_num = int(input("Введите число "))
#             if user_num == rnd_num:
#                 print("Ура, вы угадали!")
#                 return 
#             print("Вы не угадали")
#     return wrapper

# def guess_num2(turns: int) -> Callable:
#     def wrapper(rnd_num: int):
#         for _ in range(turns):
#             user_num = int(input("Введите число "))
#             if user_num == rnd_num:
#                 print("Ура, вы угадали!")
#                 return 
#             print("Вы не угадали")
#     return wrapper

# Задание №2
# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# из диапазонов.


def main(func: Callable):
    def wrapper(rnd_num, turns: int, *args, **kwargs): 
        if rnd_num < 1:
            rnd_num = 1
        elif rnd_num > 100:
            rnd_num = 100 
        if turns < 1:
            turns = 1
        elif turns > 10:
            turns = 10

        print(f'Игра началась!')
        result = func(rnd_num, turns, *args, **kwargs)
        print(f'Игра завершена')
        
        return result

    return wrapper

@main
def guess(rnd_num: int, turns: int) -> int: 
    for _ in range(turns):
            user_num = int(input("Введите число ")) 
            if user_num == rnd_num:
                print("Ура, вы угадали!")
                break 
            print("Вы не угадали") 
    
            
guess(-5, 100) 



