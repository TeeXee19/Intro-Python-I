"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

cMonth = datetime.today().month
cYear = datetime.today().year

cal = calendar.TextCalendar(calendar.SUNDAY)

def newCal(a=cMonth, b=cYear):
	return cal.formatmonth(b, a)

c = sys.argv

if len(c) == 1:
	print(newCal(cMonth, cYear))
elif len(c) == 2:
	try:
		int(c[1])
		month =int(c[1])
		print(newCal(month))
	except ValueError:
		print('Invalid input! Please Enter an Interger')
elif len(c)	== 3:
	try:
		int(c[1]) and int(c[2])
		month = int(c[1])
		year = int(c[2])
		print(newCal(month, year))
	except ValueError:
		print('Please enter a valid month and year in integer')
else:
	print('Plase use the format (cal.py mm yyyy)')