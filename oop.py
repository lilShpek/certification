# Задание №1
# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.

# from math import pi


# class Circle:
#     def __init__(self, radius: float):
#         self.radius = radius

#     def get_length(self):
#         return 2 * pi * self.radius

#     def get_square(self):
#         return pi * self.radius ** 2


# new_circle = Circle(3)
# print(new_circle.get_length())
# print(new_circle.get_square())



# Задание №2
# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.



# class Rectangle():
#     def __init__(self, *args):
#         self.side_1 = args[0]
#         if len(args) > 1:
#             self.side_2 = args[1]
#         else:
#             self.side_2 = args[0]

#     def square(self):
#         return self.side_2 * self.side_1

#     def perimetr(self):
#         return (self.side_2 + self.side_1) * 2


# a = Rectangle(10, 15).square()
# b = Rectangle(20).perimetr()
# print(a, b)




# Задание №3
# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.



# class People():

#     def __init__(self, first_name, second_name, patronymic, yaer, pol, city):
#         self.first_name = first_name
#         self.second_name = second_name
#         self.patronymic = patronymic
#         self.__yaer = yaer
#         self.pol = pol
#         self.city = city

#     def birthday(self):
#         self.__yaer += 1

#     def full_name(self):
#         return self.first_name + '\t' + self.second_name + '\t' + self.patronymic

#     def get_year(self):
#         return self.__yaer


# Vasa = People('Вася', 'Петров', 'Николаевич', 20, 'Мужской', 'Сочи')
# Vasa.birthday()
# print(Vasa.get_year(), Vasa.full_name())




# Задание №4
# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь


# class Employer(People):
#     def __init__(self, first_name, second_name, patronymic, yaer, pol, city, ID):
#         super().__init__(first_name, second_name, patronymic, yaer, pol, city)
#         if len(str(ID)) == 6 and type(ID) == int:
#                 self.ID = ID

#         else:
#             self.ID = 100000

#     def get_level(self):
#         level = (sum(int(i) for i in str(self.ID))) % 7
#         self.level = level
#         return self.level

# Vasya = Employer('Вася', 'Петров', 'Николаевич', 20, 'Мужской', 'Сочи', 123487)
# Vasya.get_level()
# print(Vasya.level)



# Задание №5
# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

# Задание №6
# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс
# Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.



# class Animals:
#     def __init__(self, weight, age, height):
#         self.weight = weight
#         self.age = age
#         self.height =height

#     def eat(self):
#         print('Ням ням!!!')

# class Birds(Animals):
#     def __init__(self, weight, age, height, size_of_wings):
#         super().__init__(weight, age, height)
#         self.size_of_wings = size_of_wings

#     def fly(self, distance):
#         print(f'I was fly on {distance} kilometres)))')

# class Predator(Animals):
#     def __init__(self, weight, age, height, power):
#         super().__init__(weight, age, height)
#         self.power = power

#     def absorb(self, victim):
#         if victim.size_of_wings > self.power:
#             print('Птичка убежала')
#         else:
#             print('Птичку съели')





# snegir = Birds(1, 1, 0.2, 12)
# snegir.eat()
# snegir.fly(100)
# tiger = Predator(100, 3, 80, 34)
# tiger.absorb(snegir)
# snegir.eat()


