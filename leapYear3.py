def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

def days_in_month(year, month):
    if month < 1 or month > 12:
        return None
    elif month == 2:
        return 29 if is_year_leap(year) else 28
    else:
        if month in (1, 3, 5, 7, 8, 10, 12):
            return 31
        else:
            return 30

def day_of_year(year, month, day):
    if month < 1 or month > 12:
        return None

    maxDays = days_in_month(year, month)

    if day < 1 or day > maxDays:
        return None

    total_days = 0
    for i in range(1, month):
        total_days += days_in_month(year, i)
        print(total_days)

    total_days += day

    return total_days


print(day_of_year(2000, 12, 31))
