# -*- coding: utf-8 -*-
"""assignment2_real-world-scheduling-scenario

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IcldX-S1xtOuMgXNfJoQ4B-rc9baridx
"""

class Patient:
    def __init__(self, name, arrival_time, treatment_time, urgency_level):
        self.name = name
        self.arrival_time = arrival_time
        self.treatment_time = treatment_time
        self.urgency_level = urgency_level

def FCFS(patients):
    return sorted(patients, key=lambda x: x.arrival_time)

def SJF(patients):
    return sorted(patients, key=lambda x: x.treatment_time)

def PS(patients):
    return sorted(patients, key=lambda x: -x.urgency_level)

def RR(patients, q=10):
    queue = []
    time = 0
    order = []

    while patients or queue:
        available = [p for p in patients if p.arrival_time <= time]
        queue.extend(available)
        for p in available:
            patients.remove(p)

        if queue:
            current_patient = queue.pop(0)
            if current_patient.treatment_time > q:
                time += q
                current_patient.treatment_time -= q
                queue.append(current_patient)
            else:
                time += current_patient.treatment_time
                order.append(current_patient)
        else:
            time += 1

    return order

patients = [
    Patient('P1', 0, 30, 3),
    Patient('P2', 10, 20, 5),
    Patient('P3', 15, 40, 2),
    # Add more patients as needed
]

print("FCFS:", [p.name for p in FCFS(patients)])
print("SJF:", [p.name for p in SJF(patients)])
print("PS:", [p.name for p in PS(patients)])
print("RR:", [p.name for p in RR(patients)])