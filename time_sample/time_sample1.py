'''
Created on Jun 26, 2017

@author: xuananh
'''
import datetime
import time
import dateutil.parser # pip install python-dateutil
from dateutil.tz import tzutc

print(dateutil.parser.parse('2008-09-03T20:56:35.450686Z')) # RFC 3339 format
print(datetime.datetime(2008, 9, 3, 20, 56, 35, 450686, tzinfo=tzutc()))

print(dateutil.parser.parse('2008-09-03T20:56:35.450686')) # ISO 8601 extended format
print(datetime.datetime(2008, 9, 3, 20, 56, 35, 450686))

print(dateutil.parser.parse('20080903T205635.450686')) # ISO 8601 basic format
print(datetime.datetime(2008, 9, 3, 20, 56, 35, 450686))

print(dateutil.parser.parse('20080903')) # ISO 8601 basic format, date only
print(datetime.datetime(2008, 9, 3, 0, 0))

my_time = dateutil.parser.parse("2018-06-06T08:01:53.420Z")
print(my_time)
print(my_time.strftime("%Y-%m-%d %H:%M:%S"))

# print(datetime.datetime.strptime("2008-09-03 20:56:35.450686+00:00", '%Y-%m-%d %H:%M:%S'))


print('==============================')
timestr = time.strftime("[%Y-%m-%d]-[%H:%M:%S]")
print("111111111111111111 {}".format(timestr))

#=============================================
start = datetime.datetime.now()
print("22222222222222222 start = {}".format(start))
print("22222222222222222 start = {}".format(start.strftime("[%Y-%m-%d]-[%H:%M:%S]")))

print('....spleeping 3s...')
time.sleep(3)
 
now = datetime.datetime.now()
print("33333333333333333 now = {}".format(now))
print("33333333333333333 now = {}".format(now.strftime("[%Y-%m-%d]-[%H:%M:%S]")))

period = (now - start).seconds
print("44444444444444444 period = {}".format(period))

datetime_7_day_ago = datetime.datetime.now() - datetime.timedelta(days=7)
print("55555555555555555 date_7_day_ago = {}".format(datetime_7_day_ago))
print("55555555555555555 now = {}".format(datetime_7_day_ago.strftime("[%Y-%m-%d]-[%H:%M:%S]")))

today = datetime.date.today()
print('666666666 today = {}'.format(today))

date_7_day_ago = today - datetime.timedelta(days=7)
print('666666666 date_7_day_ago = {}'.format(date_7_day_ago))




