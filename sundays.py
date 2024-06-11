def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def count_sundays():

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    current_day_od_week = 2

    sunday_count = 0
    for year in range(1901, 2001):
        for month in range(12):
            if current_day_od_week == 0:
                sunday_count += 1

            if month == 1 and is_leap_year(year):
                current_day_od_week += 29
            else:
                current_day_od_week += days_in_month[month]

            current_day_od_week %= 7 

    return sunday_count
    
sundays_on_first = count_sundays()
print(f"Number of Sundays that fell on the first of the month during the 20th century: {sundays_on_first}")
