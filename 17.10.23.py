# t1=(12,342,True,'Hello',"bye",3.14,43.23,1123.3,False,False)

# d=dict()

# for item in t1 :
#     key=type(item)
#     if key in d :
#         d[key].append(item)
#     else :
#         d[key]=[item]

# print(d)


# my_list = ['hello', 1, 2, 1,2, 'hello', False, 1]
# for item in set(my_list):
#     if my_list.count(item) == 2:
#         my_list.remove(item)
#         my_list.remove(item)
# print(my_list)



# Задание №6
# Погружение в Python | Коллекции
# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.


text = 'слова был один  пробел между ним и номером строки'
text = text.split()
text.sort()
max_lenght = max([len(i) for i in text])
for counter, value  in enumerate(text, start = 1):
    
   print(f'{counter} {value:>{max_lenght}}')


# Задание №7
# Погружение в Python | Коллекции
# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях.

# text = 'или не совпадают в ваших решениях Объясните почему они совпадают'
# text = text.replace(' ','')
# my_dict = {char: text.count(char) for char in text}
    
# print(my_dict)



# def search_friend(item, hike):
#     for key,value in hike.items():
#         if item not in value:
#             return key

# hike = {
# 'Aaz': ("спички", "спальник", "дрова", "топор"),
# 'Skeeve': ("спальник", "спички", "вода", "еда"),
# 'Tananda': ("вода", "спички", "косметичка"),
# }
# all_items = {}
# for key,value in hike.items():
#     for item in value:
#         if item in all_items:
#             all_items[item] += 1
#         else:
#             all_items[item] = 1

# print(all_items)

# res = ""
# for key,value in all_items.items():
#     if value == len(hike):
#         res += key + " "

# print(f"Вещи, которые взяли все - {res}")

# res = ""
# for key,value in all_items.items():
#     if value == 1:
#         res += key + " "

# print(f"Вещи, которые уникальные - {res}")

# res = ""
# for key,value in all_items.items():
#     if value == len(hike) - 1:
#         res += f"это вещь - {key} и находится у {search_friend(key, hike)} \n"

# print(f"Вещи, которые есть у всех друзей кроме одного :\n{res}")