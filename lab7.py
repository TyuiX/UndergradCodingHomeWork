# Jason Zhang
# jasozhang
# 112710259
# CSE 101
# Lab Assignment 7

def check_halves(s):
    firsthalf = s[0:int((len(s)/2))]
    secondhalf = s[int(len(s)/2):int(len(s))]
    if len(firsthalf) == 0 or len(secondhalf) == 0:
        return 0
    elif firsthalf[0] == secondhalf[0]:
        return 1 + check_halves(firsthalf[1:] + secondhalf[1:])
    elif firsthalf[0] != secondhalf[0]:
        return 0
    else:
        return check_halves(firsthalf[1:] + secondhalf[1:])




