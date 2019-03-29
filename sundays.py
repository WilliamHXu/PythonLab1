def number_of_sundays():
    count = 0
    day = 2
    month = 0
    year = 1901
    while year < 2001:
        if day == 0:
            count += 1
        if month in {8, 3, 5, 10}:
            day = (day + 2) % 7
        elif month in {1}:
            day = day
        else:
            day = (day + 3) % 7
        month = (month + 1) % 12
        if month == 0:
            year += 1
    return count

print(number_of_sundays())

