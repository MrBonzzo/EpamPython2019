# -*- coding: utf-8 -*-

"""
Реализуйте метод, определяющий, является ли одна строка 
перестановкой другой. Под перестановкой понимаем любое 
изменение порядка символов. Регистр учитывается, пробелы 
являются существенными.
"""

def is_permutation(a: str, b: str) -> bool:
    # Нужно проверить, являются ли строчки 'a' и 'b' перестановками
    if len(a) != len(b):
        return False
    a_sorted = sorted(a)
    b_sorted = sorted(b)
    if a_sorted == b_sorted:
        return True
    else:
        return False

assert is_permutation('baba', 'abab')
assert is_permutation('abbba', 'abab')
