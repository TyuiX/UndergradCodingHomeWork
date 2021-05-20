# Jason Zhang
# jasozhang
# 112710259
# CSE 101
# Homework 5

from hw5_classes import *

# Part I
def treatment_cost(hospital, patient_info):
    p1 = Patient(patient_info[0], patient_info[1], patient_info[2])
    cost = 0
    if hospital.is_hospitalization_required(p1):
        cost += hospital.hospitalization_cost_day
        if hospital.is_ventilator_required(p1):
            cost += hospital.ventilator_cost_day
    return cost



# Part II
def find_remaining_ventilators(hospital, patients_info):
    vent = hospital.ventilators_available
    for i in patients_info:
        p1 = Patient(i[0], i[1], i[2])
        if hospital.is_ventilator_required(p1):
            vent -= 1
    return vent

# Part III
def find_hospitalization_count(hospital, patients_info):
    h = 0
    for i in patients_info:
        p1 = Patient(i[0], i[1], i[2])
        if hospital.is_hospitalization_required(p1):
            h += 1
            if hospital.is_ventilator_required(p1):
                h -= 1
    return h

# Part IV
def hospital_accommodation_count(hospital):
    return hospital.ventilators_available

# Part V
def non_admittable_treatable_count(hospital, patients_info):
    cap = hospital.capacity_left
    vent = hospital.ventilators_available
    untreated = 0
    full = False
    for i in patients_info:
        p1 = Patient(i[0], i[1], i[2])
        if full == False:
            if vent < 0:
                untreated += 1
            elif hospital.is_hospitalization_required(p1):
                cap -= 1
                if hospital.is_ventilator_required(p1):
                    vent -= 1

            if cap == 0:
                full = True
        else:
            untreated += 1

    return untreated