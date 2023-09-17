# lst = 'a a a b c a a d c d d'.split()
# dct = {}
# for i in lst:

#     if i not in dct:
#         print(i, end = ' ')
#     else:
#         print(f"{i}_{dct[i]}", end=" ")
#     dct[i] = dct.get(i, 0) + 1

#     Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

# txt = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.\
#     So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells".replace('.', ' ').lower().split()
# print(len(set(txt)))






