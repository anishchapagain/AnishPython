import datetime
import time
#https://strftime.org/


today = datetime.date.today()#1
#today = datetime.datetime.today()#1
print('Today    :', today)

#calculate: timedelta() #2
print('microseconds:', datetime.timedelta(microseconds=1))
print('milliseconds:', datetime.timedelta(milliseconds=1))
print('seconds     :', datetime.timedelta(seconds=1))
print('minutes     :', datetime.timedelta(minutes=1))
print('hours       :', datetime.timedelta(hours=1))
print('days        :', datetime.timedelta(days=1))
print('weeks       :', datetime.timedelta(weeks=1))

one_day = datetime.timedelta(days=1)
#print('One day  :', one_day)

yesterday = today - one_day
print('Yesterday:', yesterday)

tomorrow = today + one_day
print('Tomorrow :', tomorrow)

print('tomorrow - yesterday:', tomorrow - yesterday)
print('yesterday - tomorrow:', yesterday - tomorrow)

one_day = datetime.timedelta(days=1)
print('1 day    :', one_day)
print('5 days   :', one_day * 5)
print('1.5 days :', one_day * 1.5)
print('1/4 day  :', one_day / 4)

print("1.5 : ",today+ one_day * 1.5)

work_day = datetime.timedelta(hours=7)
meeting_length = datetime.timedelta(hours=1)
print('meetings per day :', work_day / meeting_length)

#example: future dates from week!
#for i in range(1,8):
#    print(today+datetime.timedelta(days=i))

#start...continue...stop
#x=1
#while x<=7:
#    print(today+datetime.timedelta(days=x))
#    x=x+1



# strftime  # datetime.date.today()
formatDT = "%a %b %d %H:%M:%S %Y"  ##strftime.org : y-m-d h:i:s
formatDT1 = "%A %B %d, (%y) -- %H:%M:%S -- %p -- %U , %j "  ##strftime.org : y-m-d h:i:s
today = datetime.datetime.today() #3
print('ISO     :', today)
s1 = today.strftime(formatDT) #4
print('strftime s1:', s1)
s2 = today.strftime(formatDT1) #4
print('strftime s2:', s2)

d = datetime.datetime.strptime(s1, formatDT)#5 : parsing
print('strptime d:', d)
print('strptime d-f:', d.strftime(formatDT))

#comparing
print('Times:')
t1 = datetime.time(12, 55, 0)
print('  t1:', t1)
t2 = datetime.time(13, 5, 0)
print('  t2:', t2)
print('  t1 < t2:', t1 < t2)

print('Dates:')
d1 = datetime.date.today()
print('  d1:', d1)
d2 = datetime.date.today() + datetime.timedelta(days=1)
print('  d2:', d2)
print('  d1 > d2:', d1 > d2)
print('  d1 > d2:', d1 < d2)

print('ctime  :', today.ctime())
tt = today.timetuple()
print('tuple  : tm_year  =', tt.tm_year)
print('         tm_mon   =', tt.tm_mon)
print('         tm_mday  =', tt.tm_mday)
print('         tm_hour  =', tt.tm_hour)
print('         tm_min   =', tt.tm_min)
print('         tm_sec   =', tt.tm_sec)
print('         tm_wday  =', tt.tm_wday)
print('         tm_yday  =', tt.tm_yday)
print('         tm_isdst =', tt.tm_isdst)
print('ordinal:', today.toordinal())

today = datetime.datetime.today() #3
print('ISO     :', today)

print('Year   :', today.year)
print('Mon    :', today.month)
print('Day    :', today.day)
print('Hour    :', today.hour)
print('Minute    :', today.minute)
print('Second    :', today.second)
print('MSecond    :', today.microsecond)

print("Now >> : ", datetime.datetime.now())
