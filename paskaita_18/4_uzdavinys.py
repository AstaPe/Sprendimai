from datetime import datetime


class DateUtils:
    @staticmethod
    def days_between_dates(date1, date2):
        date1_obj = datetime.strptime(date1, "%Y-%m-%d")
        date2_obj = datetime.strptime(date2, "%Y-%m-%d")
        delta = date2_obj - date1_obj
        return abs(delta.days)

    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

date1 = "2023-05-15"
date2 = "2024-03-10"
print("Number of days between", date1, "and", date2, ":", DateUtils.days_between_dates(date1, date2))

year = 2024
print("Is", year, "a leap year?", DateUtils.is_leap_year(year))
