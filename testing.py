

# Задание №1
# Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

# 19:54
# Задание №2
# Напишите для задачи 1 тесты doctest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)



def delete_not_english(text: str):
    """
    Эта функция, которая удаляет из текста все символы
    кроме букв латинского алфавита и пробелов.
    Возвращается строка в нижнем регистре.
    >>> delete_not_english('qwerty')
    'qwerty'
    >>> delete_not_english('QWERTY')
    'qwerty'
    >>> delete_not_english('QWERTY!@#$%^')
    'qwerty'
    >>> delete_not_english('QWE RTY')
    'qwe rty'
    >>> delete_not_english('QWE RTY йцгнупйцгшупйцу')
    'qwe rty '
    >>> delete_not_english('QWE RTY йцгнупйцгшупйцу 98444 !"№;%:?*(')
    'qwe rty   '
    """
    rez = ''
    text = text.lower()
    for i in text:
        if ord(i) in range(97, 123) or i == ' ':
            rez = rez + i
    return rez

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod(verbose=True)





# Задание №3
# Напишите для задачи 1 тесты unittest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

# 20:19
# Задание №4
# Напишите для задачи 1 тесты pytest. Проверьте следующие
# варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

import unittest


class TestDeleteNotEnglish(unittest.TestCase):
    def test_1(self):
        self.assertEqual('qwerty', delete_not_english('qwerty'))

    def test_2(self):
        self.assertEqual('qwerty', delete_not_english('QWERTY'))

    def test_3(self):
        self.assertEqual('qwerty', delete_not_english('QWERTY!@#$%^'))

    def test_4(self):
        self.assertEqual('qwe rty', delete_not_english('QWE RTY'))

    def test_5(self):
        self.assertEqual('qwe rty ', delete_not_english('QWE RTY йцгнупйцгшупйцу'))

    def test_6(self):
        self.assertEqual('qwe rty   ', delete_not_english('QWE RTY йцгнупйцгшупйцу 98444 !"№;%:?*('))


if __name__ == '__main__':
    import unittest
    unittest.main()





#pytest:


import pytest
import unittest


def test_1():
    assert 'qwerty' == delete_not_english('qwerty')


def test_2():
    assert 'qwerty' == delete_not_english('QWERTY')


def test_3():
    assert 'qwerty' == delete_not_english('QWERTY!@#$%^')


def test_4():
    assert 'qwe rty' == delete_not_english('QWE RTY')


def test_5():
    assert 'qwe rty ' == delete_not_english('QWE RTY йцгнупйцгшупйцу')


def test_6():
    assert 'qwe rty   ' == delete_not_english('QWE RTY йцгнупйцгшупйцу 98444 !"№;%:?*(')


if __name__ == '__main__':
    pytest.main()