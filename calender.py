import calendar
weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
m,d,y = map(int,input().split())
temp = calendar.weekday(y, m, d)
print(weekdays[temp])