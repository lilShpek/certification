#Номер 10
coins = input("Введите строку монет: ")
coins_orel = coins.count('O')
coins_reshka = coins.count('R')
if coins_orel>coins_reshka:
    print(f"Монет нужно перевернуть: {coins_reshka}")
elif coins_orel<coins_reshka:
    print(f"Монет нужно перевернуть: {coins_orel}")
else:
    print("Количество монет с орлом и решкой равно")

#Номер 12
# S = int(input("Введите сумму S: "))
# P = int(input("Введите произведение P: "))
# for x in range(1, 1001):
#     y = S - x
#     if x*y == P:
#         print(f"Числа x и y: {x}, {y}")
#         break   
# else: 
#     print("Нет действительных значений x и y")

#Номер 14
# n = int(input())
# a = 0
# c = 1
# while c<=n:
#     print(c, end=' ')
#     a += 1
#     c = 2**a
# print()
