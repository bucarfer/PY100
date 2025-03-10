'''The Python documentation for the datetime module provides two attributes to retrieve the year from a date or datetime object: year and isocalendar.

from datetime import date
today = date.today()

today_year = today.year
iso_year = today.isocalendar()[0]

What is the difference between the year attribute and the isocalendar method?'''

#the year attribute retrieves the year of the date provided (Gregorian calendar)

#The ISO calendar returns the ISO year, ISO week number, and ISO weekday. The ISO year does not always match the calendar year. It starts on the first Monday of the week that is at least 4 days long, which could be the last 4 days of December.

from datetime import date

d1 = date(2023, 12, 31)
d2 = date(2024, 1, 1)

print(f'calendar year: {d1.year}') #calendar year: 2023
print(f'calendar year: {d2.year}') #calendar year: 2024

print(f'ISO year d1: {d1.isocalendar()}') #ISO year d1: 2023
print(f'ISO year d2: {d2.isocalendar()}') #ISO year d2: 2024

#in this case doesnt happen since the last day of the year is Sunday and the first day of the year is Monday, the lat day of the year should be Monday, Tuesday, or Wednesday for that date to be part of the next ISO year. 