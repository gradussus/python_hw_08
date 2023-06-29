from datetime import datetime, timedelta
from collections import defaultdict


users = [
    {"name": "user 1", "birthday": datetime(1998, 7, 21)},
    {"name": "user 2", "birthday": datetime(1995, 7, 22)},
    {"name": "user 3", "birthday": datetime(1888, 6, 23)},
    {"name": "user 4", "birthday": datetime(1999, 6, 24)},
    {"name": "user 5", "birthday": datetime(2000, 6, 25)},
    {"name": "user 6", "birthday": datetime(1966, 6, 28)},
    {"name": "user 7", "birthday": datetime(1646, 6, 29)},
    {"name": "user 8", "birthday": datetime(2023, 7, 27)},
    {"name": "user 9", "birthday": datetime(1324, 7, 1)},
    {"name": "user 10", "birthday": datetime(2001, 7, 2)},
    {"name": "user 11", "birthday": datetime(2000, 7, 3)},
    {"name": "user 12", "birthday": datetime(2020, 6, 30)},
]

def get_birthdays_per_week(users):
    print('sadf')

    today = datetime.today().date()
    
    end_date = today + timedelta(days=7)

    birthday_dict = defaultdict(list)

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()

        birthday = birthday.replace(year=today.year)
        
        if today <= birthday < end_date:
            birthday_weekday = birthday.strftime("%A")
            if birthday.weekday() >= 5:
                birthday_weekday = "Monday"
            print(birthday_weekday)
            birthday_dict[birthday_weekday].append(name)
    print(birthday_dict)

get_birthdays_per_week(users)