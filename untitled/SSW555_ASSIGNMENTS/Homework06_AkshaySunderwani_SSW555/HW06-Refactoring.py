# -*- coding: utf-8 -*-


'''
    Demonstrate refactoring on the following code.   You may rewrite the code from Python into your favorite lanaguage
    but you must demonstrate at least two separate refactorings to improve the readability and maintainability.

    Use your favorite unit test framework to  demonstrate wthat the
    refactorings don't change, and don't break the functionality.

    The domain for this task is similar to the GEDCOM project but simplified for this assignment.

    For the record, this code is intentionally UGLY to encourage you to refactor it to make it better!

'''

import datetime

target1 = datetime.date(2000, 1, 1)
target2 = datetime.date(2016, 10, 3)

# dates is a list of dates
dates = [
    datetime.date(2010, 1, 15),
    datetime.date(2012, 6, 29),
    datetime.date(1953, 2, 23),
    datetime.date(1969, 3, 29),
    datetime.date(1994, 8, 24)
]


# loop through each of the dates and compare to the target2
for date in dates:
    # print number of days between date and target11
    if target1 > date:
        print('There are', (target1 - date).days, 'days between', target1, 'and', date)
    else:
        print('There are', (date - target1).days, 'days between', target1, 'and', date)

    # print number of days between date and target11
    if target2 > date:
        print('There are', (target2 - date).days, 'days between', target2, 'and', date)
    else:
        print('There are', (date - target2).days, 'days between', target2, 'and', date)

    # Assume there are 30.4 days per month
    if target1 > date:
        print('There are', int((target1 - date).days / 30.4), 'months between', target1, 'and', date)
    else:
        print('There are', int((date - target1).days / 30.4), 'months between', target1, 'and', date)

    # Assume there are 30.4 days per month
    if target2 > date:
        print('There are', int((target2 - date).days / 30.4), 'months between', target2, 'and', date)
    else:
        print('There are', int((date - target2).days / 30.4), 'months between', target2, 'and', date)

    # Assume there are 365.25 days per year
    if target1 > date:
        print('There are', int((target1 - date).days / 365.25), 'years between', target1, 'and', date)
    else:
        print('There are', int((date - target1).days / 365.25), 'years between', target1, 'and', date)

    if target2 > date:
        print('There are', int((target2 - date).days / 365.25), 'years between', target2, 'and', date)
    else:
        print('There are', int((date - target2).days / 365.25), 'years between', target2, 'and', date)



# I sure wish someone would write some units to test this code.  That would help to validate the logic
# would make refactoring easier


