# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#


def leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    
    day_from_year = 0
    for y in range(year1, year2+1):
        if leap_year(y):
            day_from_year = day_from_year + 366
        else:
            day_from_year = day_from_year + 365
            
    day_from_month = 0
    if leap_year(year1):
        days_of_months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for m in range(0, month1-1):
            day_from_month = day_from_month - days_of_months[m]
    else:
        days_of_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for m in range(0, month1-1):
            day_from_month = day_from_month - days_of_months[m]
    if leap_year(year2):
        days_of_months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for m in range(month2-1, 12):
            day_from_month = day_from_month - days_of_months[m]
    else:
        days_of_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for m in range(month2-1, 12):
            day_from_month = day_from_month - days_of_months[m]
    
    
    day_from_day = day2 - day1
        
    print("From Year: ", day_from_year)
    print("From Month: ", day_from_month)
    print("From Day: ", day_from_day)
    total_days = day_from_year + day_from_month + day_from_day
    print("Total Day(s): ", total_days)
    return total_days


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")

test()

# additional test

def additional_test():
    test_cases = [((2018,9,5,2020,7,1), 665)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")    
            
additional_test()