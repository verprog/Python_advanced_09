# Создайте класс ПЕРСОНА с абстрактными методами, позволяющими
# вывести на экран информацию о персоне, а также определить ее возраст (в
# текущем году). Создайте дочерние классы: АБИТУРИЕНТ (фамилия, дата
# рождения, факультет), СТУДЕНТ (фамилия, дата рождения, факультет, курс),
# ПРЕПОДАВАТЕЛЬ (фамилия, дата рождения, факультет, должность, стаж),
# со своими методами вывода информации на экран и определения возраста.
# Создайте список из n персон, выведите полную информацию из базы на
# экран, а также организуйте поиск персон, чей возраст попадает в заданный
# диапазон.
from abc import ABC,abstractmethod
from datetime import date
import datetime
import time
from dateutil.relativedelta import relativedelta

# Функция которая вычисяет кол-во прошедших от заданой даты



# get_diff_years('24.07.1983')


class Person:
    def __init__(self, birthday):
        self._birthday = birthday

    @staticmethod
    def get_diff_years(p_day):
        now = datetime.datetime.today().date()
        try:
            befor = datetime.datetime.strptime(p_day, '%d.%m.%Y').date()
        except SyntaxError:
            return 'Invalid date!! Please enter a date in the format DD.MM.YYYY\n'
        except ValueError as ex:
            return ex
        else:
            diff_years = relativedelta(now, befor).years
            return diff_years

    @abstractmethod
    def get_age(self):
        age = Person.get_diff_years(self._birthday)
        return age

    @abstractmethod
    def get_info(self):
        pass


class Abiturient(Person):
    def __init__(self, lastname, birthday, faculty):
        self._lastname = lastname
        super().__init__(birthday)
        self._faculty = faculty

    def get_info(self):
        return f"class: {self.__class__.__name__}\n Фамилия: {self._lastname}\n Возраст: {self.get_age()}\n Факультет: {self._faculty}"


class Student(Person):
    def __init__(self, lastname, birthday, faculty, course):
        self._lastname = lastname
        super().__init__(birthday)
        self._faculty = faculty
        self._course = course

    def get_info(self):
        return f"class: {self.__class__.__name__}\n Фамилия: {self._lastname}\n Возраст: {self.get_age()}\n Факультет: {self._faculty}\n Курс: {self._course}"

class Teacher(Person):
    def __init__(self, lastname, birthday, faculty, position,experience):
        self._lastname = lastname
        super().__init__(birthday)
        self._faculty = faculty
        self._position = position
        self._experience = experience

    def get_info(self):
        return f"class: {self.__class__.__name__}\n Фамилия: {self._lastname}\n Возраст: {self.get_age()}\n Факультет: {self._faculty}\n Должность: {self._position}\n Стаж: {self._experience}"


ab = Abiturient('Бандерос', '24.07.2001', 'Коммуникации')
st = Student('Родригес', '05.12.1991', 'Математики и информатики', 4)
st1 = Student('Джоли', '05.12.1999', 'Искусствоведения', 1)
te = Teacher('Тарантино', '01.05.1976', 'Искусствоведения', 'Декан', 15)

data = [ab, st, st1, te]

print('>>> Вывод всех персон ', '>' * 30)
for i in data:
    print(i.get_info())
    print('*'*30)

print('>>> Поиск в диапазоне ', '>' * 30)
for i in data:
    if i.get_age() >= 20 and  i.get_age() <= 40:
        print(i.get_info())
        print('*'*30)




