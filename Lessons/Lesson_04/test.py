import datetime
import pandas
from dateutil.relativedelta import relativedelta


def get_diff_years(p_day):
    now = datetime.datetime.today().date()
    try:
        befor = datetime.datetime.strptime(p_day, '%d.%m.%Y').date()
    except SyntaxError:
        return print('Invalid date!! Please enter a date in the format DD.MM.YYYY\n')
    except ValueError as ex:
        return print(ex)
    else:
        diff_years = relativedelta(now, befor).years
        return print(diff_years)

get_diff_years('24.13.1983')