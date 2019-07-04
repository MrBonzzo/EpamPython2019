"""
Представьте, что вы пишите программу по формированию и выдачи комплексных обедов для сети столовых, которая стала
расширяться и теперь предлагает комплексные обеды для вегетарианцев, детей и любителей китайской кухни.

С помощью паттерна "Абстрактная фабрика" вам необходимо реализовать выдачу комплексного обеда, состоящего из трёх
позиций (первое, второе и напиток).
В файле menu.yml находится меню на каждый день, в котором указаны позиции и их принадлежность к
определенному типу блюд.

"""
import yaml


class Menu:
    def __init__(self, day):
        self.day = day
        with open('menu.yml', 'r', encoding='utf-8') as menu_file:
            self.menu = yaml.safe_load(menu_file)[day]

    def get_first_course(self):
        return self.menu['first_courses']

    def get_second_course(self):
        return self.menu['second_courses']

    def get_drink(self):
        return self.menu['drinks']

    def get_lunch(self):
        lunch = {}
        lunch['first_course'] = self.get_first_course()
        lunch['second_course'] = self.get_second_course()
        lunch['drink'] = self.get_drink()
        return lunch


class VeganMenu(Menu):
    def __init__(self, day):
        super().__init__(day)
        self.menu = {course: self.menu[course]['vegan']
                     for course in self.menu}


class ChildMenu(Menu):
    def __init__(self, day):
        super().__init__(day)
        self.menu = {course: self.menu[course]['child']
                     for course in self.menu}


class ChinaMenu(Menu):
    def __init__(self, day):
        super().__init__(day)
        self.menu = {course: self.menu[course]['china']
                     for course in self.menu}


if __name__ == '__main__':

    vegan = VeganMenu('Friday').get_lunch()
    print((f"Vegan lunch on Friday:\n\t{vegan['first_course']}"
           f"\n\t{vegan['second_course']}\n\t{vegan['drink']}"))

    child = ChildMenu('Monday').get_lunch()
    print((f"Child lunch on Monday:\n\t{child['first_course']}"
           f"\n\t{child['second_course']}\n\t{child['drink']}"))

    china = ChinaMenu('Wednesday').get_lunch()
    print((f"China lunch on Wednesday:\n\t{china['first_course']}"
           f"\n\t{china['second_course']}\n\t{china['drink']}"))
