# import random


# def search(lower, top, count):
#     chislo = random.randint(lower, top)
#     numder = int(input('Введите число: '))
#     while count > 0:
#         if numder > chislo:
#             print('меньше')
#             count -= 1

#         elif numder < chislo:
#             print('больше')
#         else:
#             print('урааа, угадал')
#             return True

#         count -= 1
#         numder = int(input('Введите число ещё раз: '))
#     print('Неугадал')
#     return False


# if __name__ == "__main__":
#     print(search(1, 10, 3))




# Задание №4
# � Создайте модуль с функцией внутри.
# � Функция получает на вход загадку, список с возможными
# вариантами отгадок и количество попыток на угадывание.
# � Программа возвращает номер попытки, с которой была
# отгадана загадка или ноль, если попытки исчерпаны.


# def riddle(str_text: str, answer: list, count, index_correct: int):
#     print(f'загадка - {str_text}\nВарианты ответа - {answer}')
#     attempt = 1
#     while attempt <= count:
#         index = int(input('Введите индекс ответа: '))
#         if index == index_correct:
#             print('верно')
#             return attempt
#         else:
#             print('неверно')
#             attempt += 1

#     print('вы истратили все попытки и проиграли')
#     return 0


# def keeping():
#     d = {'Зимой и летом одним цветом': [0, 'Ель', 'Берёза', 'Дуб'],
#          '33 подружки в ровный ряд стоят, Их перемешай, они заговорят.': [0, 'Алфавит', 'зубы', 'люди'],
#          'Если дождик с неба льет, Тебе поможет всегда...': [1, 'бег', 'зонт', 'чудо']}
#     for key, value in d.items():
#         n = riddle(key, value[1:], 2, value[0])
#         save_result(key, n, output_d)


# # добовляем в словарь значение загадка - ответ
# def save_result(text, num, output_d: dict):
#     output_d[text] = num


# output_d = {}

# if __name__ == "__main__":
#     keeping()
#     print(output_d)