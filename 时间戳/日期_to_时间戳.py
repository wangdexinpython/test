import datetime,time

ss = '2019-06-21 16:35'
timeArray = time.strptime(ss, "%Y-%m-%d %H:%M")
timeStamp = int(time.mktime(time.strptime(ss, "%Y-%m-%d %H:%M")))
