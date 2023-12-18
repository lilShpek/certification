# Задание №1
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)


from datetime import datetime



class MyString:
    
    def __init__(self, author,value = None):
        self.author = author
        self.create_time = datetime.now()
        if not value:
            self.value = ''
        else:
            self.value =value

s1 = MyString('Vasya')
print(s1.value)



# Задание №2
# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра


# class Archive:

#     _instance = None

#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#             cls._instance.archive_text = []
#             cls._instance.archive_number = []
#         else:
#             cls._instance.archive_text.append(cls._instance.text)
#             cls._instance.archive_number.append(cls._instance.number)
#         return cls._instance

#     def __init__(self, text: str, number: int | float):
#         self.text = text
#         self.number = number



# Задание №3
# Добавьте к задачам 1 и 2 строки документации для классов.


# Задание №4
# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.



# class Archive:

#     # _instance = None

#     # def __new__(cls, *args, **kwargs):
#     #     if cls._instance is None:
#     #         cls._instance = super().__new__(cls)
#     #         cls._instance.archive_text = []
#     #         cls._instance.archive_number = []
#     #     else:
#     #         cls._instance.archive_text.append(cls._instance.text)
#     #         cls._instance.archive_number.append(cls._instance.number)
#     #     return cls._instance


#     def __init__(self, text: str, number: int | float):
#         self.text = text
#         self.number = number

#     def __str__(self):
#         return f'Это экземпляр класса архив'
    
#     def __repr__(self):
#         return f'Это архив с информацией {self.text} и числом {self.number}'
    
# a1 = Archive('Привет, мир', 52)
# a2 = Archive('Пока, мир', 35)
# a3 = Archive('Как дела?', 777)
# print(a1)
# print(repr(a1))
# print([a1, a2])





# Задание №5
# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.


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
    
#     def __str__(self):
#         return f'Это прямоугольник со сторонами {self.width} и {self.height}'
    
#     def __eq__(self, other):
#         if self.area() == other.area():
#             return True
#         else:
#             return False
    
    
    
    

# r1 = Rectangle(3, 3)
# r2 = Rectangle(4.5, 2)
# # r3 = r1 + r2
# # print(r3)
# # print(r2 - r1)
# print(r1 == r2)




