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

    cls.counter = 0
    cls_new_ = cls.__new__

    def __new__(cls, *args, **kwargs):
        cls.counter += 1
        return cls_new_(cls, *args, **kwargs)

    @classmethod
    def get_created_instances(cls):
        return cls.counter

    @classmethod
    def reset_instances_counter(cls):
        counter_before_reset = cls.counter
        cls.counter = 0
        return counter_before_reset

    cls.__new__ = __new__
    cls.get_created_instances = get_created_instances
    cls.reset_instances_counter = reset_instances_counter

    return cls


@instances_counter
class User:
    pass


if __name__ == '__main__':

    print(User.get_created_instances())  # 0
    user, _, _ = User(), User(), User()
    print(user.get_created_instances())  # 3
    print(user.reset_instances_counter())  # 3
    print(user.get_created_instances())  # 0
