class Patient:
    def __init__(self, name, age, previous_conditions):
        self.age = age
        self.name = name
        self.previous_conditions = previous_conditions


class Doctor:
    def __init__(self, id):
        self.id = id
        self.capacity_left = 5
        self.patients = []

    def is_doctor_busy(self):
        return self.capacity_left == 0

    def assign_patient(self, patient):
        if self.capacity_left > 0:
            self.patients.append(patient)
            self.capacity_left -= 1


class Hospital:
    def __init__(self, capacity, ventilators, doctor_count, hospitalization_cost_day=1000, ventilator_cost_day=1200):
        self.capacity_left = capacity
        self.ventilators_available = ventilators
        self.hospitalization_cost_day = hospitalization_cost_day
        self.ventilator_cost_day = ventilator_cost_day
        self.doctors = [Doctor(i) for i in range(doctor_count)]

    def is_hospitalization_required(self, patient):
        return patient.previous_conditions or patient.age > 65

    def is_ventilator_required(self, patient):
        return patient.previous_conditions and patient.age > 75

    def admit_patient(self, patient):
        if self.is_ventilator_required(patient) and self.ventilators_available > 0:
            self.ventilators_available -= 1
            self.assign_doctor(patient)
        elif not self.is_ventilator_required(patient):
            self.assign_doctor(patient)

    def assign_doctor(self, patient):
        for doctor in self.doctors:
            if not doctor.is_doctor_busy():
                doctor.assign_patient(patient)

    def __repr__(self):
        return f'Hospital({self.capacity_left}, {self.ventilators_available}, {len(self.doctors)}, ' \
               f'{self.hospitalization_cost_day}, {self.ventilator_cost_day})'

    def __str__(self):
        return self.__repr__()