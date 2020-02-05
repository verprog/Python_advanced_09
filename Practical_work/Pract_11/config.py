from enum import Enum


TOKEN = 'СВОЙ токен введи:)'


class States(Enum):
    S_START = 0  # Начало нового диалога
    FULL_NAME = 1
    NUMBER_PHONE = 2
    MAIL = 3
    ADDRESS = 4
    WISHES = 5
    STOP = 6
