import pandas as pd
import copy as copy

df = pd.read_csv("current_wildfiredata.csv")

deployable_units = {
    "Fire Engines": [60, 2000, 10],
    "Ground Crews": [90, 3000, 8],
    "Smoke Jumpers": [30, 5000, 5],
    "Helicopters": [45, 8000, 3],
    "Tanker Planes": [120, 15000, 2]
}

deployable_units_copy = copy.deepcopy(deployable_units)

damageCosts = {
    "low": 50000,
    "medium": 100000,
    "high": 200000
}

def countUnits():
    num_global = 0
    for key, value in deployable_units.items():
        num_local = value[2]
        num_global += num_local
    return num_global

def countFires():
    num_fires = len(df)
    return num_fires

def countFiresAddressed():
    num_units = countUnits()
    num_fires = countFires()
    if num_units <= num_fires:
        num_fires_addressed = num_units
    else:
        num_fires_addressed = num_fires
    return num_fires_addressed

def countFiresDelayed():
    num_units = countUnits()
    num_fires = countFires()
    if num_units < num_fires:
        num_fires_delayed = num_fires - num_units
    else:
        num_fires_delayed = 0
    return num_fires_delayed

def singleOperationCost():
    for key, value in deployable_units_copy.items():
        deployable = value[2]
        if deployable > 0:
            value[2] = value[2] - 1
            lowest_operation_cost = value[1]
            return lowest_operation_cost

def totalOperationCost():
    total_operation_cost = 0
    num_fires_addressed = countFiresAddressed()
    for i in range(num_fires_addressed):
        single_operation_cost = singleOperationCost()
        total_operation_cost += single_operation_cost
    return total_operation_cost

def damageCost():
    damage_cost = 0
    num_fires = countFires()
    num_fires_addressed = countFiresAddressed()
    for i in range(num_fires_addressed, num_fires):
        severity = df.at[i,"severity"]
        if severity == "high":
            damage_cost += damageCosts["high"]
        elif severity == "medium":
            damage_cost += damageCosts["medium"]
        elif severity == "low":
            damage_cost += damageCosts["low"]
    return damage_cost

def severityReport():
    num_fires = countFires()
    severity_report = {'low': 0, 'medium': 0, 'high': 0}
    for i in range(num_fires):
        severity = df.at[i,"severity"]
        if severity == "low":
            severity_report["low"] += 1
        elif severity == "medium":
            severity_report["medium"] += 1
        elif severity == "high":
            severity_report["high"] += 1
    return severity_report

# Number of fires addressed: X
print(countFiresAddressed())
# Number of fires delayed: X
print(countFiresDelayed())
# Total operational costs: X
print(totalOperationCost())
# Estimated damage costs from delayed responses: X
print(damageCost())
# Fire severity report: {'low': X, 'medium': X, 'high': X}
print(severityReport())
