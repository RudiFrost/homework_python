from datetime import datetime


def f(d, m, y):
    fullmonth = [1, 3, 5, 7, 8, 10, 12]
    medmonth = [4, 6, 9, 11]
    current_datetime = datetime.now()
    d_now = current_datetime.day
    m_now = current_datetime.month
    y_now = current_datetime.year
    if (y > 0 and m > 0 and d > 0 and m < 13 and d < 32) and (y <= y_now):
        if (y < y_now) or (y == y_now and m < m_now) or (y == y_now and m == m_now and d <= d_now):
            if d < 31 and m in medmonth:
                return "Было такое"
            elif d < 32 and m in fullmonth:
                return "Было такое"
            elif m == 2:
                if (d == 29 and y % 4 == 0) or d < 29:
                    return "Было такое"
    return "._."


print(f(29, 2, 2021))
