"""
Реализовать дескриптор, кодирующий слова с помощью шифра Цезаря

"""


class ShiftDescriptor:

    def __init__(self, shift):
        self.shift = shift

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        temp_value = [chr((ord(c) - ord('a') + self.shift) % 26 + ord('a'))
                      for c in list(value)]
        self.value = ''.join(temp_value)


class CeasarSipher:

    message = ShiftDescriptor(4)
    another_message = ShiftDescriptor(7)

if __name__ == '__main__':
    a = CeasarSipher()
    a.message = 'abc'
    a.another_message = 'hello'

    assert a.message == 'efg'
    assert a.another_message == 'olssv'
