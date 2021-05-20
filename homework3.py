# Jason Zhang
# jasozhang
# 112710259
# CSE 101
# Homework 3

import math


# Part I
def calculate_journey_duration(has_forest, has_river, has_mountain):
    day = 0
    if has_river == True and has_forest == True and has_mountain == True:
        day = -1
    else:
        if has_forest == False and has_river == False and has_mountain == False:
            day += 1
        else:
            if has_mountain == True:
                day += 2
                if has_river == True:
                    day += 3
            if has_forest == True or has_river == True:
                day += 2
    return day




# Part II
def break_check_points(check_points):
    seg = []
    for i in check_points:
        if 3 < i < 7:
            for x in range(2):
                seg.append(i//2)
        elif 7 <= i < 10:
            for y in range(3):
                seg.append(i//3)
        elif i == -1 or i >= 10:
            seg.append('N/A')
        else:
            seg.append(i)
    return seg


# Part III
def check_points_possible(segments, initial_energy, num_muffins):
    energy = initial_energy + (num_muffins*2)
    checkpoint = 0
    for i in segments:
        energy -= i
        if energy >= 0:
            checkpoint += 1
    if energy == 0:
        checkpoint -= 1
    return checkpoint



# Part IV
def days_for_target(initial_weight, target_weight):
    weight = initial_weight
    target_reach = False
    days = 0
    wdays = 0
    while target_reach == False:
        days += 1
        wdays += 1
        if wdays < 6:
            weight -= 10
        elif wdays >= 6:
            weight += 8
            if wdays == 7:
                wdays = 0
        if weight <= target_weight:
            target_reach = True
    return days



# Part V
def count_remaining_items(ingredients_needed, items_at_home):
    total_needed = len(ingredients_needed)
    for i in ingredients_needed:
        for x in items_at_home:
            if i == x:
                total_needed -= 1
    return  total_needed
