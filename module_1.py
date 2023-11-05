from datetime import datetime
from sys import argv

#use terminal -> python ./module_1.py DD.MM.YYYY


def date_validate(date: str) -> bool:
    try:
        data_format = datetime.strptime(date, "%d.%m.%Y").date()
        return True
    except:
        return False


def check_leap_year(date: str) -> bool:
    year = int(date.split(".")[-1])
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(date_validate('29.02.2023'))
    print(check_leap_year('29.02.2000'))
    print(date_validate(argv[1]))
    print(check_leap_year(argv[1]))