

def get_reach_taks(balance):
    if balance > 5_000_000:
        balance *= 0.9
    return balance

def add_money(balance):
    balance = get_reach_taks(balance)
    success = False
    value = int(input('Введите сумму пополнения: '))
    if value % 50 == 0:
        balance += value
        success = True
    else:
        print('Введите сумму, кратную 50.')
    return balance, success

def calc_comiss(value):
    result = value * 0.015
    if result < 30:
        result = 30
    if result > 600:
        result = 600
    return result

def get_money(balance):
    balance = get_reach_taks(balance)
    success = False
    value = int(input('Введите сумму для снятия: '))
    if value % 50 == 0:
        comiss = calc_comiss(value)
        if balance >= (comiss + value):
            balance = balance - value - comiss
            success = True
        else:
            print('У вас недостаточный баланс.')
    else:
        print('У вас некорректная сумма денег.')
    return balance, success

count = 0
balance = 0
while True:
    print('1 - пополнить баланс \n 2 - Снять деньги \n 3 - Выход')
    sel = int(input('Сделайте ваш выбор: '))
    if sel == 1:
        balance, success = add_money(balance)

    elif sel == 2:
        balance, success = get_money(balance)

    elif sel == 3:
        break

    else:
        print('Введите корректный выбор команды.')

if success:
    count += 1
print(f'Ваш баланс составляет: {balance}')

