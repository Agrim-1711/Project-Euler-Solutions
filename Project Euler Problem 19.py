#Problem 19
#https://projecteuler.net/problem=19
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)

import calendar

count = 0
for y in range(1901,2001):
  for m in range(1,13):
    if calendar.weekday(y,m,1) == 6:
      count += 1

print(f"{count} Sundays fell on the first of the month during the 20th century!")