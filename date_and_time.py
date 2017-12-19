from calendar import day_name, weekday


if __name__ == '__main__':
    month, day, year = list(map(int, input().split(' ')))
    print(day_name[weekday(year, month, day)].upper())
