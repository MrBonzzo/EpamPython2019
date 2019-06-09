"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""
import functools


def instances_counter(cls):

    class DecoratorClass(cls):
        cls.counter = 0

        def __init__(self):
            cls.counter += 1
            super().__init__()

        @staticmethod
        def get_created_instances():
            return cls.counter

        @staticmethod
        def reset_instances_counter():
            counter_before_reset = cls.counter
            cls.counter = 0
            return counter_before_reset

    return DecoratorClass


@instances_counter
class User:
    pass


if __name__ == '__main__':

    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
    user.get_created_instances()  # 0
