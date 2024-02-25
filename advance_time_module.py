from datetime import datetime
from datetime import timedelta


def today(txt_file):
    with open(txt_file, 'r') as file:
        today_to_str = file.read().strip()
    today_datetime = datetime.strptime(today_to_str, '%Y-%m-%d').date()
    message = f"Today is {today_datetime}"
    print(message)
    return today_datetime


def advance_day(days_to_advance):
    with open('today.txt', 'r') as file:
        today_to_str = file.read().strip()

    today_datetime = datetime.strptime(today_to_str, '%Y-%m-%d')

    timedelta_obj = timedelta(days=days_to_advance)
    advance_day = today_datetime + timedelta_obj
    advance_day_to_string = datetime.strftime(advance_day, '%Y-%m-%d')
    return advance_day_to_string

    

