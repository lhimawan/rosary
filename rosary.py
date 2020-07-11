import datetime, webbrowser
from datetime import timedelta

#Get today's day of the week
Today = datetime.datetime.now()
DayOfWeek = Today.weekday() #0 = Monday, 6 = Sunday
Year = Today.year

#check if today is in Lent season
def IsLent(Today):
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
    
    #Calculate DaysToEaster, given FullMoon & Year
    YearIndex = Year % 19
    DaysToEaster = abs(6 - FullMoon[YearIndex].weekday())
    if DaysToEaster == 0:
        DaysToEaster = 7

    #Calculate Easter & Ash Wednesday dates
    Easter = FullMoon[YearIndex] + timedelta(days=DaysToEaster)
    AshWednesday = Easter - timedelta(days=46)

    #return value
    if Today >= AshWednesday and Today < Easter:
        return True
    else:
        return False

#check if today is Advent or Christmas
def IsAdventXmas(Today):
    #get weekday() of Christmas
    Christmas = datetime.date(Year, 12, 25)
    ChristmasDay = Christmas.weekday()

    #count 4th Advent Sunday from Christmas
    LastAdvent = Christmas - timedelta(days = ChristmasDay + 1)
    #count 1st Advent Sunday
    FirstAdvent = LastAdvent - timedelta(days = 21)

    #return value
    if Today >= FirstAdvent and Today <= Christmas:
        return True
    else:
        return False

#set Mysteries to open webbrowser
def JoyfulMysteries():
    webbrowser.open('https://www.rosarycenter.org/homepage-2/rosary/how-to-pray-the-rosary/joyful-mysteries-without-distractions/')
def LuminousMysteries():
    webbrowser.open('https://www.rosarycenter.org/homepage-2/rosary/how-to-pray-the-rosary/luminous-without-distractions/')
def SorrowfulMysteries():
    webbrowser.open('https://www.rosarycenter.org/homepage-2/rosary/how-to-pray-the-rosary/sorrowful-without-distractions/')
def GloriousMysteries():
    webbrowser.open('https://www.rosarycenter.org/homepage-2/rosary/how-to-pray-the-rosary/glorious-without-distractions/')

#Flow control - logic for mysteries
if DayOfWeek == 6:
    if IsLent(Today):
        SorrowfulMysteries()
    elif IsAdventXmas(Today):
        JoyfulMysteries()
    else:
        #Other Sundays
        GloriousMysteries()
elif DayOfWeek == 0 or DayOfWeek == 5:
    JoyfulMysteries()
elif DayOfWeek == 1 or DayOfWeek == 4:
    SorrowfulMysteries()
elif DayOfWeek == 2:
    GloriousMysteries()
elif DayOfWeek == 3:
    LuminousMysteries()
