
#http://pandas.pydata.org/pandas-docs/stable/10min.html
#fileHandling : http://python-course.eu/file_management.php
#os, sys : http://www.thomas-cokelaer.info/tutorials/python/module_os.html
#pymotw

from datetime import datetime
import time

print ("time.ctime() : ",time.ctime())
hrfromnow = time.time() + 60 * 60
print ("time.ctime() + 1hr : ",time.ctime(hrfromnow))

#named tuple
val = time.gmtime()
print ("time.gmtime() : ",time.gmtime())
print ("time.gmtime() >> : ",val.tm_year,val.tm_mon)


print("\nDateTime >> ")
print("Now >> : ", datetime.now())
print("Today >> : ",datetime.today())
print("Datetime ctime Today : ", datetime.ctime(datetime.today()))
nowagain = datetime.today().timetuple()
print("Nowagain : ",nowagain.tm_year, nowagain.tm_mon)
print(nowagain)

now = time.time()
print("Now time.time() : ",now)

print ("The time . time() : ",time.time())
print ("The time . clock() : ",time.clock())


date1= "1/20/2017"
date2= "3/20/2017"
newdate1 = time.strptime(date1,"%m/%d/%Y")
newdate2 = time.strptime(date2,"%m/%d/%Y")
if(newdate2 < newdate1):
    print (date2," is greater than ",date1)
    print (newdate2," is greater than ",newdate1)


jan = "1/1/2017"
today = datetime.today()
if time.strptime(jan,"%m/%d/%Y") < time.strptime(str(datetime.today()),"%m/%d/%Y"):
    print("TODAY >> ",datetime.today())