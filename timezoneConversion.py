import datetime
import pytz

t = input("enter time (format eg: 12:30 am): ")
tz = input("enter timezone (est/cst/mst/pst/ist): ")
print("You entered:",t,tz)
t = "2012 1 1 " + t    # explicity mentioning these dates as default older date will have different timezone values 
# (https://stackoverflow.com/questions/11442183/pytz-timezone-shows-weird-results-for-asia-calcutta/11442571#:~:text=1%20Answer&text=Time%20zones%20change%20over%20the,zone%20to%20an%20actual%20date.)

tz_dict = {"est":"EST","cst":"us/central","mst":"MST","pst":"us/pacific","ist":"asia/kolkata"}

t1 = pytz.timezone(tz_dict[tz]).localize(datetime.datetime.strptime(t,"%Y %m %d %I:%M %p"))

print("EST will be:",datetime.datetime.strftime(t1.astimezone(pytz.timezone("EST")),"%I:%M %p"))
print("CST will be:",datetime.datetime.strftime(t1.astimezone(pytz.timezone("us/central")),"%I:%M %p"))
print("MST will be:",datetime.datetime.strftime(t1.astimezone(pytz.timezone("MST")),"%I:%M %p"))
print("PST will be:",datetime.datetime.strftime(t1.astimezone(pytz.timezone("us/pacific")),"%I:%M %p"))
print("IST will be:",datetime.datetime.strftime(t1.astimezone(pytz.timezone("Asia/Kolkata")),"%I:%M %p"))

