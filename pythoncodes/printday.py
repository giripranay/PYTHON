import calendar

month,day,year=map(int,input().split())

print(calendar.weekday(year, month, day))
