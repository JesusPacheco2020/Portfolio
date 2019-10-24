# Age in Seconds Program
# This program will calculate a person's approximate in seconds

import datetime

# Program Greeting
print ('This program computes the approximate age in seconds of an')
print ('individual based on a provided date of birth. Only ages for')
print ('dates of birth from 1900 and after can be computed\n')

# get month, day, year of birth
month_birth = int(input('Enter month born (1-12): '))
day_birth = int(input ('Enter day born (1-31): '))
year_birth = int(input('Enter year born: (4-digit): '))

# get current month, day, year
current_month = datetime.date.today().month
current_day = datetime.date.today().day
current_year = datetime.date.today().year

# determine number of seconds in a day, average month and average year
numsecs_day = 24 * 60 * 60
numsecs_year = 365 * numsecs_day

avg_numsecs_year = ((4 * numsecs_year) + numsecs_day) // 4
avg_numsecs_month = avg_numsecs_year // 12

# calculate approximate age in seconds
numsecs_1900_dob = (year_birth - 1900) * avg_numsecs_year + \
                    (month_birth - 1) * avg_numsecs_month + \
                    (day_birth * numsecs_day)

numsecs_1900_today = (current_year - 1900) * avg_numsecs_year + \
                    (current_month - 1) * avg_numsecs_month + \
                    (current_day * numsecs_day)

age_in_secs = numsecs_1900_today - numsecs_1900_dob

# output results
print ('\nYou are approximately', age_in_secs, 'seconds old')

