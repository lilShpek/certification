# import argparse

# def quadratic_equations(a, b, c):
#     d = b ** 2 - 4 * a * c
#     if d > 0:
#         return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
#     if d == 0:
#         return -b / (2 * a)
#     return None


# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='Solving quadratic equations')
#     parser.add_argument('param', metavar='a b c', type=float, nargs=3,
#     help='enter a b c separated by a space')
#     args = parser.parse_args()
# print(quadratic_equations(*args.param))


# Задание №1
# Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.


import logging
from datetime import datetime


logging.basicConfig(filename='project3.log',
                    encoding='utf-8',
                    level=logging.NOTSET)
logger = logging.getLogger('калькулятор')


def calc(s):
    logger.info(f"Пользователь {name} ввел строку {s}")
    try:
        print(f"Результат равен {eval(s)}")
        logger.info(f"результат вычисления равен {eval(s)}")
    except ZeroDivisionError as e:
        print(e)
        logger.critical(f"{datetime.now().strftime('%H:%M:%S')} произошла ошибка {e}")


name = input("Введите свое имя ")
while True:
    s = input("Введите арифметическое выражение ")
    if s != "exit":
        calc(s)
    else:
        print("Спасибо за пользование нашим калькулятором!")
        break

