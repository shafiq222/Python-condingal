import random
import time

def getrandomdate(startdate,enddate):
    print("lading a date",startdate,"new date",enddate)
    randomgenerator = random.random()
    dateformat = "%m/%d/%Y"
    starttime = time.mktime(time.strptime(startdate,dateformat))
    endtime = time.mktime(time.strptime(enddate,dateformat))

    randomtime = starttime + randomgenerator * (endtime -  starttime)
    randomdate = time.strftime(dateformat,(time.localtime(randomtime)))
    return randomdate
print("random date is",getrandomdate("1/1/2026","5/27/2027"))