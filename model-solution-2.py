# For AI Model Training https://youtu.be/29ZQ3TDGgRQ?si=D72UOyhjeHQdENxY
import numpy as np
import pandas as pd

# Import historical environmental data
historical_environmental = pd.read_csv("historical_environmental_data.csv")

# Import historical wildfire data
historical_wildfire = pd.read_csv("historical_wildfiredata.csv")

# Convert dataframe columns to string to compare them together without conflict
historical_environmental["timestamp"] = historical_environmental["timestamp"].astype(str)
historical_wildfire["timestamp"] = historical_wildfire["timestamp"].astype(str)

# For the environmental data, create a new fire risk dataframe
    #  by creating a new column for fire_risk which is 0 by default
historical_fire_risk = historical_environmental.assign(fire_risk=0)

# For every row in wildfire, if the timestamp is found in environmental data, set the fire_risk to 1
index_environment = len(historical_environmental)
index_wildfire = len(historical_wildfire)
num_wildfire = 0
for x in range(index_environment):
    for y in range(index_wildfire):
        timestamp_fire_risk = historical_fire_risk.at[x,"timestamp"]
        timestamp_wildfire = historical_wildfire.at[y,"timestamp"]
        if timestamp_fire_risk == timestamp_wildfire:
            historical_fire_risk.at[x,"fire_risk"] = 1
            # Count
            num_wildfire += 1
            print("Found one")
            break

print("Fire Risk Column Calculated")
print("Number of matching timestamps:", num_wildfire)
historical_fire_risk.to_csv("ProcessedData.csv")



