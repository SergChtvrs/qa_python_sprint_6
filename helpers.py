import random
from datetime import datetime
from calendar import monthrange
from data import AboutRentData


def format_locators(locator_a, num):
    method, locator = locator_a
    locator = locator.format(num)
    return method, locator


def customer_generator():
    customer = {
        'name': random.choice(['Вася', 'Петя', 'Никола', 'Уолтер', 'Геральт', 'Томас']),
        'last_name': random.choice(['Шелби', 'Иванов', 'Питонов', 'Уайт', 'Эскобар', 'Тесла']),
        'address': random.choice(['Луна', 'Сатурн', 'Венера'])+' '+str(random.randint(10, 99)),
        'metro': random.choice(['Крылатское', 'Полянка', 'Кунцевская',
                                        'Славянский бульвар', 'Электрозаводская', 'Профсоюзная']),
        'mobile': f'+7{random.randint(100000000, 999999999)}'
    }
    return customer


def rent_date_generator():
    current_date = datetime.now()
    days_in_month = monthrange(current_date.year, current_date.month)[1]
    r_day = random.randint(current_date.day, days_in_month)
    r_date = f'{r_day}.{current_date.month}.{current_date.year}'
    rent_date = {
        'day': r_day,
        'date': r_date
        }
    return rent_date


def about_generator():
    about = {'colour': random.choice(AboutRentData.colour),
             'period': random.choice(AboutRentData.period),
             'comment': AboutRentData.comment
             }
    return about
