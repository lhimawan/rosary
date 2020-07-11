#Returns datetime.date of Easter Sunday, given Year
#https://mathlair.allfunandgames.ca/easter.php
import datetime
from datetime import timedelta

#Year = datetime.datetime.now().year
Year = 2020

#List of Paschal Full Moon Dates
FullMoon = [
    datetime.date(Year,4,14),
    datetime.date(Year,4,3),
    datetime.date(Year,3,23),
    datetime.date(Year,4,11),
    datetime.date(Year,3,31),
    datetime.date(Year,4,18),
    datetime.date(Year,4,8),
    datetime.date(Year,3,28),
    datetime.date(Year,4,16),
    datetime.date(Year,4,5),
    datetime.date(Year,3,25),
    datetime.date(Year,4,13),
    datetime.date(Year,4,2),
    datetime.date(Year,3,22),
    datetime.date(Year,4,10),
    datetime.date(Year,3,30),
    datetime.date(Year,4,17),
    datetime.date(Year,4,7),
    datetime.date(Year,3,27)
    ]

#Calculate DaysToSunday, given FullMoon & Year
YearIndex = Year % 19
DaysToEaster = abs(6 - FullMoon[YearIndex].weekday())
if DaysToEaster == 0:
    DaysToEaster = 7

#Return Easter Sunday
Easter = FullMoon[YearIndex] + timedelta(days=DaysToEaster)
print(Easter)
