import calendar


def get_calendar(year, month):
    c = calendar.TextCalendar(calendar.SUNDAY)
    print(c.formatmonth(year, month))


get_calendar(2025, 1)
