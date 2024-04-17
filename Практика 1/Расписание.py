import datetime



def chek_year(year):

    if (year%4 == 0 and year%100 != 0) or (year%400==0):
        return True
    return False
countWeekends = int(input())
year = int(input())
leapYear = chek_year(year)
code_year = (6 + (year%100) + (year%100)//4)%7
weeks= [0 for i in range(7)]

for i in range(countWeekends):

    day, month = input().split()
    
    if month == 'January':
        week = datetime.datetime(year, 1, int(day)).weekday()
    elif month == 'February':
        week = datetime.datetime(year, 2, int(day)).weekday()
    elif month == 'March':
        week = datetime.datetime(year, 3, int(day)).weekday()
    elif month == 'April':
        week = datetime.datetime(year, 4, int(day)).weekday()
    elif month == 'May':
        week = datetime.datetime(year, 5, int(day)).weekday()
    elif month == 'June':
        week = datetime.datetime(year, 6, int(day)).weekday()
    elif month == 'July':
        week = datetime.datetime(year, 7, int(day)).weekday()
    elif month == 'August':
        week = datetime.datetime(year, 8, int(day)).weekday()
    elif month == 'September':
        week = datetime.datetime(year, 9, int(day)).weekday()
    elif month == 'October':
        week = datetime.datetime(year, 10, int(day)).weekday()
    elif month == 'November':
        week = datetime.datetime(year, 11, int(day)).weekday()
    elif month == 'December':
        week = datetime.datetime(year, 12, int(day)).weekday()
    weeks[week] -= 1
    
beginWeekday = input()
if beginWeekday == 'Monday':
    numberWeek = 0
elif beginWeekday == 'Tuesday':
    numberWeek = 1
elif beginWeekday == 'Wednesday':
    numberWeek = 2
elif beginWeekday == 'Thursday':
    numberWeek = 3
elif beginWeekday == 'Friday':
    numberWeek = 4
elif beginWeekday == 'Saturday':
    numberWeek = 5
elif beginWeekday == 'Sunday':
    numberWeek = 6
i = 0
if leapYear:
    while i <= 6:
        if i == 0 and numberWeek == 6:
            weeks[i] += 53
        elif i == numberWeek:
            weeks[i] += 53
            if i  < 6:
                i += 1
                weeks[i] += 53
        else:
            weeks[i] += 52
        i += 1
else:
    while i <= 6:
        
        if i == numberWeek:
            weeks[i] += 53
            
        else:
            weeks[i] += 52
        i += 1
bestWeekdayNumber, bestWeekday,worseWeekdayNumber, worseWeekday= 0, 0, 0, 60
for j in range(7):
    day = weeks[j]
    if day > bestWeekday:
        bestWeekday = day
        bestWeekdayNumber = j
    if day < worseWeekday:
        worseWeekday = day
        worseWeekdayNumber = j
result_1, result_2 = '', ''
if bestWeekdayNumber == 0:
    result_1 = 'Monday'
elif bestWeekdayNumber == 1:
    result_1 = 'Tuesday'
elif bestWeekdayNumber == 2:
    result_1 = 'Wednesday'
elif bestWeekdayNumber == 3:
    result_1 = 'Thursday'
elif bestWeekdayNumber == 4:
    result_1 = 'Friday'
elif bestWeekdayNumber == 5:
    result_1 = 'Saturday'
elif bestWeekdayNumber == 6:
    result_1 = 'Sunday'

if worseWeekdayNumber == 0:
    result_2 = 'Monday'
elif worseWeekdayNumber == 1:
    result_2 = 'Tuesday'
elif worseWeekdayNumber == 2:
    result_2 = 'Wednesday'
elif worseWeekdayNumber == 3:
    result_2 = 'Thursday'
elif worseWeekdayNumber == 4:
    result_2 = 'Friday'
elif worseWeekdayNumber == 5:
    result_2 = 'Saturday'
elif worseWeekdayNumber == 6:
    result_2 = 'Sunday'
print(result_1, result_2)