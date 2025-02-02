import pandas as pd
df = pd.read_csv("current_wildfiredata.csv")

deployableUnits = {
    "Smoke Jumpers": [30, 5000, 5],
    "Fire Engines": [60, 2000, 10],
    "Helicopters": [45, 8000, 3],
    "Tanker Planes": [120, 15000, 2],
    "Ground Crews": [90, 3000, 8]
}

damageCosts = {
    "low": 50000,
    "mid": 100000,
    "high": 200000
}

def countUnits():
    num_global = 0
    for key, value in deployableUnits.items():
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

# Number of fires addressed: X
print(countFiresAddressed())
# Number of fires delayed: X
print(countFiresDelayed())
# Total operational costs: X
# Estimated damage costs from delayed responses: X
# Fire severity report: {'low': X, 'medium': X, 'high': X}
