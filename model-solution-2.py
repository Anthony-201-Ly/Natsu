# For AI Model Training https://youtu.be/29ZQ3TDGgRQ?si=D72UOyhjeHQdENxY
import pandas as pd

# Import historical environmental data
historical_environmental = pd.read_csv("historical_environmental_data.csv")

# Import historical wildfire data
historical_wildfire = pd.read_csv("historical_wildfiredata.csv")

# Compare environmental and wildfire data
# This allows us to see whether the environmental data results in a wildfire
historical_environmental.join(other=historical_wildfire, on="timestamp", how="left")
# ^^^ Error trying to merge on object and int64 columns
print(historical_environmental)
# Split data to X and y (independant and dependant)



