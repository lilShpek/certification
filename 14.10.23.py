# txt = input('Введите текст: ')
# if txt.isdigit():
#     txt = int(txt)
#     print(bin(txt))
#     print(oct(txt))
#     print(hex(txt))
# else: 
#     print(txt.isascii())




# data = [21, 32.2, True, 'привет', 32.2]
# for i, v in enumerate(data):
#     result1 = "это целое число" if type(v) is int else ''
#     result2 = "это строка" if isinstance(v, str) else ''
#     print(i + 1, v, id(v), v.__sizeof__(), hash(v), result1, result2)