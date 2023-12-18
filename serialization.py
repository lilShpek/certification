# Задание №1
# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.


# import json


# def get_info():
#     array = {}

#     with open('results.txt', 'r', encoding='UTF-8') as f:
#         for line in f:
#             name, digit = line.split()
#             print(name, digit)
#             name = name.capitalize()
#             if name in array:
#                 array[name].append(float(digit))
#             else:
#                 array[name] = [float(digit)]
#     with open('next_results.json', 'w', encoding='UTF-8') as f:
#         json.dump(array, f, ensure_ascii=False, indent=2)
# get_info()

# Задание №2
# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.


# import os
# import json

# def baza():
#     if os.path.isfile("next_users.json"):
#         try:
#             with open('next_users.json', 'r', encoding='UTF-8') as f:
#                 # Проверка на пустой файл или некорректные данные JSON
#                 try:
#                     array = json.load(f)
#                 except json.JSONDecodeError:
#                     array = {}
#                 print(array)
#         except FileNotFoundError:
#             print("Ошибка: файл 'next_users.json' не найден.")
#     else:
#         array = {}

#     s = set()

#     while True:
#         name = input('Введите имя: ')
#         if name == 'exit':
#             break
#         indef = (input("Введите личный идентификатор: "))
#         if indef in s:
#             print('такой айди есть, введите другой')
#             continue
#         else:
#             s.add(indef)
#         level = (input("Введитеуровень доступа (от 1 до 7): "))

#         if int(level) > 7 or int(level) < 1:
#             print("Введите кооректнвй уровень доступа")
#             continue
#         if level in array:
#             array[level][indef] = name
#         else:
#             array[level] = {indef: name}

#     print(array)
#     with open('next_users.json', 'w', encoding='UTF-8') as f:
#         json.dump(array, f, ensure_ascii=False, indent=2)

# baza()



# # Задание №3
# # Напишите функцию, которая сохраняет созданный в
# # прошлом задании файл в формате CSV.

# import csv


# def csv_rename():
#     users = []

#     with open('next_users.json', 'r', encoding='UTF-8') as f:
#         array = json.load(f)

#     for level, val in array.items():
#         for indev, name in val.items():
#             users.append({'level': level, 'indev': indev, 'name': name})

#     with open('next_users.csv', 'w', newline='', encoding='UTF-8') as f:
#         csv_write = csv.DictWriter(f, fieldnames=["level", "indev", "name"], dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
#         csv_write.writeheader()
#         csv_write.writerows(users)


# csv_rename()



# Задание №4
# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.


def complement_csv_rename():
    dict_cl = {}
    mass = []
    with open('next_users.csv', 'r', encoding='UTF-8', newline='') as f:
        array = csv.reader(f, dialect='excel')
        for i, line in enumerate(array):
            if i == 0:
                continue
            dict_cl = {}
            print(line)
            level, indev, name = line
            dict_cl['level'] = level
            dict_cl['indev'] = f"{int(indev):010}"
            dict_cl['name'] = name.title()
            dict_cl['hash'] = hash(f"{dict_cl['name']}{dict_cl['indev']}")
            mass.append(dict_cl)
        print(mass)
    with open('users.json', 'w', encoding='UTF-8') as f:
        json.dump(mass, f, ensure_ascii=False, indent=2)

complement_csv_rename()