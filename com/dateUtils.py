import datetime as dt
import calendar as cl


def getTime(days,date):
    "获取时间字符串"
    dateTypeStr= ""
    if date == None:
        date = dt.datetime.now()+dt.timedelta(days=days)
        dateTypeStr = date.strftime('%Y-%m-%d')
    else:
        dateTypedt = dt.datetime.strptime(date,'%Y-%m-%d')

def getYesterDayTime():
    "获取昨天的字符串"
    date = dt.datetime.now()+dt.timedelta(days=-1)
    dateTypeStr = date.strftime('%Y-%m-%d')
    return dateTypeStr

def getTenYearsAgoTime():
    "获取昨天的字符串"
    date = dt.datetime.now()+dt.timedelta(days=-3650)
    dateTypeStr = date.strftime('%Y-%m-%d')
    return dateTypeStr

def getDateFromStr(date):
    dateTypedt = dt.datetime.strptime(date, '%Y/%m/%d')
    return dateTypedt


