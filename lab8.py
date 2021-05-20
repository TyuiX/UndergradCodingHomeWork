# Jason Zhang
# jasozhang
# 112710259

# CSE 101
# Lab Assignment 8

def number_of_sets(day, day_exercise, time_exercise):
    if day == 'Sun' or day == 'Sat':
        return 0
    else:
        return 60 // (time_exercise[day_exercise[day]])
