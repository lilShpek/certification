# Задание №1
# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.


# from collections import deque


# class Factorial:
#     def __init__(self, k=1):
#         self.memory = deque(maxlen=k)

#     def __call__(self, n, *args, **kwargs):
#         result = 1
#         for i in range(2, n + 1):
#             result *= i
#         self.memory.append({n: result})
#         return self.memory[-1]

#     def old(self):
#         return self.memory
    

# a = Factorial()

# print(a(100))

# with a as f:
#     print(f)
    
# #     №2
# # Доработаем задачу 1.
# # Создайте менеджер контекста, который при выходе
# # сохраняет значения в JSON файл.

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         dump_dict = {}
#         while self.memory:
#             dump_dict.update(self.memory.popleft())
#         with open(f'{int(time.time())}', 'w', encoding='utf-8') as f:
#             json.dump(dump_dict, f)


# Задание №3
# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.


# class Factorial:
#     def __init__(self, start, stop, step=1):
#         self.start = start
#         self.stop = stop
#         self.step = step

#     def __iter__(self):
#         return self

#     def __next__(self):
#         while self.start < self.stop:
#             result = 1
#             for i in range(2, self.start + 1):
#                 result *= i
#             self.start += self.step
#             return result
#         raise StopIteration


# a = Factorial(15, 20, 2)

# for i in a:
#     print(i)


# Задание №4
# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений
# (отрицательных).
# Используйте декораторы свойств.


# class Rectangle:

#     def __init__(self, width, height=None):
#         self.width = width
#         if height is None:
#             self.height = width
#         else:
#             self.height = height

#     def perimeter(self):
#         return 2 * (self.width + self.height)

#     def area(self):
#         return self.width * self.height
    
#     def __add__(self, other):
#         all_perimetr = self.perimeter() + other.perimeter()
#         width = self.width + other.width 
#         height = all_perimetr/2 - width
#         return Rectangle(width, height)
    
#     def __sub__(self, other):
#         new_perimeter = self.perimeter() - other.perimeter() 
#         if new_perimeter < 0:
#             self, other = other, self
#             new_perimeter = -new_perimeter
#         width = abs(self.width - other.width)
#         height = abs(new_perimeter/2 -width)
#         return Rectangle(width, height)
    
#     @property
#     def width(self):
#         return self.__width

#     @property
#     def height(self):
#         return self.__height

#     @width.setter
#     def width(self, value):
#         if value > 0:
#             self.__width = value
#         else:
#             raise ValueError('Величина должна быть положительной')
#     @height.setter
#     def height(self, value):
#         if value>0:
#             self.__height = value
#         else:
#             raise ValueError('Величина должна быть положительной')


# r1 = Rectangle(5, 7)
# print(r1.width)

# r1.height = 100
# print(r1.height)





# class Range:
#     def __init__(self, min_value: int = None, max_value: int = None):
#         self.min_value = min_value
#         self.max_vaue = max_value

#     def __set_name__(self, owner, name):
#         self.param_name = '_' + name

#     def __get__(self, instance, owner):
#         return getattr(instance, self.param_name)

#     def __set__(self, instance, value):
#         self.validate(value)
#         setattr(instance, self.param_name, value)

#     def __delete__(self, instance):
#         raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

#     def validate(self, value):

#         if not isinstance(value, int):
#             raise TypeError(f'Значение {value} должно быть целым числом')
#         if value <= 0:
#             raise ValueError('Физическая величина должна быть больше 0')


# class Rectangle:
#     width = Range()
#     height = Range()

#     def __init__(self, width, height=None):
#         self.width = width
#         if height is None:
#             self.height = width
#         else:
#             self.height = height

#     def perimeter(self):
#         return 2 * (self.width + self.height)

#     def area(self):
#         return self.width * self.height


# r1 = Rectangle(15, 20)
# r1.width = 1000
# print(r1.width)