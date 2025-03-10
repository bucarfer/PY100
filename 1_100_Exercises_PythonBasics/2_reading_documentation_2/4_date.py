'''Using the datetime module in Python, how would you obtain the current date and time? '''

# using datetime.now(), naive = (no tzinfo)
from datetime import datetime
naive_now = datetime.now()
print(f'time in Santo Domingo with naive_now: {naive_now}')

# using timezone and timedelta, aware = (with tzinfo)
from datetime import timezone, timedelta
aware_now = datetime.now(timezone(timedelta(hours=-4)))
print(f'time in Santo Domingo with aware_now: {aware_now}')

# using zoneinfo path (if using Python 3.9+)
# list of tz database time zones (Wikipedia) https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
from zoneinfo import ZoneInfo
now_santodomingo = datetime.now(ZoneInfo('America/Santo_Domingo'))
print (f'time in Santo Domingo with zoneinfo: {now_santodomingo}')
