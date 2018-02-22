import datetime

start, stop = datetime.date(1901, 1, 1), datetime.date(2000, 12, 31)
sundayCount = 0

while start < stop:
    if start.weekday() == 6 and start.day == 1:
        sundayCount += 1
    start += datetime.timedelta(days=1)

print(sundayCount)
