#Returns datetime.date of 4 Advent Sundays, given Year
import datetime
from datetime import timedelta

#set year to test
Year = 2017
#get weekday() of Christmas
Christmas = datetime.date(Year, 12, 25)
ChristmasDay = Christmas.weekday()

#count 4th Advent Sunday from Christmas
Advent = []
Advent.append (Christmas - timedelta(days = ChristmasDay + 1))

#count first 3 Advent Sundays
for i in range(1,4):
    Advent.append (Advent[0] - timedelta(days = 7 * i))
    
#reverse list to get ascending order
Advent.reverse()

#print test results
print ('The 4 Advent Sundays of the year are:')
for i in range(len(Advent)):
    print (Advent[i])
print ('And Christmas is on ' + str(ChristmasDay))
