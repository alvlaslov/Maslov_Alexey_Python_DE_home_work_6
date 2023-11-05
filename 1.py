"""
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
"""
#use terminal -> python ./1.py DD.MM.YYYY

from module_1 import date_validate
from module_1 import check_leap_year
from datetime import datetime
from sys import argv

print(argv)
print(date_validate(argv[1]))
print(check_leap_year(argv[1]))