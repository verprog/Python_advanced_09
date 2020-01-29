from enum import Enum


TOKEN = '988581457:AAGTtV81u_YTzQwOf6qG6yvDRGmQNJw0-PQ'


class States(Enum):
    S_START = 0  # Начало нового диалога
    FULL_NAME = 1
    NUMBER_PHONE = 2
    MAIL = 3
    ADDRESS = 4
    WISHES = 5
    STOP = 6
