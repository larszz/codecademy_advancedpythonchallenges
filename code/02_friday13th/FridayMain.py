import datetime

import global_objects.InputHandler as ih
import calendar

day_to_check: int = 13
weekday_to_check: str = "Friday"


def day_is_weekday(year: int, month: int, day: int, weekday: str) -> bool:
    day_date = datetime.date(year, month, day)
    return day_date.strftime("%A") == weekday


def month_has_friday_the_thirteenth(year: int, month: int) -> bool:
    return day_is_weekday(year, month, day_to_check, weekday_to_check)


if __name__ == '__main__':
    print(month_has_friday_the_thirteenth(23, 10))
    print(month_has_friday_the_thirteenth(23, 11))
    print(month_has_friday_the_thirteenth(23, 12))
    print(month_has_friday_the_thirteenth(23, 1))
    print(month_has_friday_the_thirteenth(22, 5))


