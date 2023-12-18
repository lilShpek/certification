# Задание №3
# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

# def get_dict_info(text: str):
#     text = list(map(int, text.split()))
#     res = {}
#     for item in text:
#         res[chr(item)] = item
#     print(res)

# get_dict_info("777 555")



# Задание №4
# ✔ Функция получает на вход произвольное количество чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

# def bubble_sort(*args):
#     res = list(args)
#     for i in range(len(res) - 1):
#         for j in range(len(res) - 1):
#             if res[j] > res[j + 1]:
#                 res[j], res[j + 1] = res[j + 1], res[j] 
#     print(res)


# bubble_sort(5,8,77,1,2,3)


# Задание №5
# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.

def calc_bonus(names: list, salaries: list, bonus_rates: list) -> dict:
    if not (isinstance(names, list) 
            and isinstance(salaries, list) and isinstance(bonus_rates, list) ):
        raise ValueError("На входе должны быть три списка!")
    if not ( len(names) == len(salaries) and len(names) == len(bonus_rates) ):
        raise ValueError("Длины списков должны быть одинаковы!")
    res = {}
    for name, salary, bonus_rate in zip(names, salaries, bonus_rates):
        res[name] = round ( salary * float(bonus_rate[:-1]) / 100, 2)
    return res




names = ["Ваня", "Вася", "Сергей"] 
salaries = [50000, 20_000, 65000]
bonus_rates = ["20.6%", "50.8%", "10.7%"]

print(calc_bonus(names, salaries, bonus_rates))


# Задание №7
# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

# def get_company_profit(budjets: dict):
#     res = []
#     for company, budjet in budjets.items():
#         res.append(sum(budjet) > 0)
#     return all(res)

    

# budjets = {"apple": [888,-777,-150,20], "VAZ": [-8,999,-7]}
# print(get_company_profit(budjets))


# data = {"один": 1, "два": 2, "три": 3} 
# x = iter(data.items()) 
# print(x) 
# y = next(x) 
# print(y) 
# z = next(iter(y)) 
# print(z)