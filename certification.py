# №1

# from typing import Callable
# import logging
# import argparse


# logging.basicConfig(filename='project1.log',
#                     encoding='utf-8',
#                     level=logging.INFO)
# logger = logging.getLogger('game')


# def main(func: Callable):
#     def wrapper(rnd_num, turns: int, *args, **kwargs):
#         try:
#             if rnd_num < 1:
#                 rnd_num = 1
#             elif rnd_num > 100:
#                 rnd_num = 100
#             if turns < 1:
#                 turns = 1
#             elif turns > 10:
#                 turns = 10

#             logging.info('Игра началась!')
#             result = func(rnd_num, turns, *args, **kwargs)
#             logging.info('Игра завершена')

#             return result
#         except Exception as e:
#             logging.error(f'Произошла ошибка: {e}')

#     return wrapper


# @main
# def guess(rnd_num: int, turns: int) -> int:
#     for _ in range(turns):
#         try:
#             user_num = int(input("Введите число "))
#             logger.info(f"Пользователь ввел число {user_num}")
#             if user_num == rnd_num:
#                 print("Ура, вы угадали!")
#                 logger.info(f"Пользователь угадал число")
#                 break
#             print("Вы не угадали")
#             logger.info("Пользователь не угадал число")
#         except ValueError:
#             logging.warning('Введите корректное число.')

#     return 0  


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description='Угадай число.')
#     parser.add_argument('rnd_num', type=int, help='Загаданное число от 1 до 100')
#     parser.add_argument('turns', type=int, help='Количество попыток от 1 до 10')

#     args = parser.parse_args()

#     guess(args.rnd_num, args.turns)



# №2
# import logging
# import argparse
# from datetime import datetime

# logging.basicConfig(filename='project2.log', encoding='utf-8', level=logging.INFO)
# logger = logging.getLogger('string')

# class MyString:
#     def __init__(self, author, value=None):
#         try:
#             self.author = str(author)
#         except Exception as e:
#             logger.error(f"Ошибка при инициализации: {e}")
#             raise

#         try:
#             self.create_time = datetime.now()
#             logger.info(f"Инициализирован объект MyString для автора '{self.author}' в {self.create_time}")
#         except Exception as e:
#             logger.error(f"Ошибка при установке времени: {e}")
#             raise

#         try:
#             if value is not None:
#                 self.value = str(value)
#             else:
#                 self.value = ''
#             logger.info(f"Установлено значение для MyString: {self.value}")
#         except Exception as e:
#             logger.error(f"Ошибка при установке значения: {e}")
#             raise

#     def __str__(self):
#         return f"MyString(author={self.author}, value={self.value}, create_time={self.create_time})"

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description='Ввод строки')
#     parser.add_argument('author', type=str, help='Имя')
#     parser.add_argument('value', type=str, nargs='?', default='', help='Значение (опционально)')

#     args = parser.parse_args()

#     try:
#         s1 = MyString(args.author, args.value)
#         logger.info(f"Объект MyString успешно создан: {s1}")
#         print(f"Значение MyString: {s1.value}")
#         logger.info(f"Программа выведет значение: {s1.value}")
#     except Exception as e:
#         logger.error(f"Ошибка при создании объекта MyString: {e}")


# №3
# import logging
# import argparse
# from datetime import datetime


# logging.basicConfig(filename='project3.log',
#                     encoding='utf-8',
#                     level=logging.NOTSET)
# logger = logging.getLogger('калькулятор')


# def calc(s):
#     logger.info(f"Пользователь {name} ввел строку {s}")
#     try:
#         print(f"Результат равен {eval(s)}")
#         logger.info(f"результат вычисления равен {eval(s)}")
#     except ZeroDivisionError as e:
#         print(e)
#         logger.critical(f"{datetime.now().strftime('%H:%M:%S')} произошла ошибка {e}")


# name = input("Введите свое имя ")
# while True:
#     s = input("Введите арифметическое выражение ")
#     if s != "exit":
#         calc(s)
#     else:
#         print("Спасибо за пользование нашим калькулятором!")
#         break

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description='Простой калькулятор')
#     parser.add_argument('--name', type=str, required=True, help='Имя пользователя')
#     args = parser.parse_args()

#     name = args.name