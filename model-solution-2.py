# For AI Model Training https://youtu.be/29ZQ3TDGgRQ?si=D72UOyhjeHQdENxY
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import folium

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

print("Warning, this might take a few minutes...")
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
            #print("Found one")
            break

#print("Fire Risk Column Calculated")
#print("Number of matching timestamps:", num_wildfire)
historical_fire_risk.to_csv("ProcessedData.csv")

# Split dataframe into X and y
y = historical_fire_risk["fire_risk"]
#print(y)

# Drop the fire_risk, timestamp, latitude, and longitude
X = historical_fire_risk.drop("fire_risk", axis=1)
X = X.drop("timestamp", axis=1)
X = X.drop("latitude", axis=1)
X = X.drop("longitude", axis=1)
#print(X)

### Training the model
# Randomly choose 20% of the dataset to be used as test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# We chose Random Forest Classifier model
# due to having to having many independant variables
# as well as having numerical values for the dependant variable (Y "whether it will be a wildfire")
# being either 0 or 1 "Random Forest Regression gave us no values of 1 for fire_risk"
rf = RandomForestClassifier()
rf.fit(X_train, y_train)

# Applying the model to make a prediction on the test data
y_rf_train_pred = rf.predict(X_train)
y_rf_test_pred = rf.predict(X_test)

#print(rf_results)

### Predict the future data

# Import future environmental data
# X -> A ||| Y -> B
future_environmental = pd.read_csv("future_environmental_data.csv")
# Drop all of the unneeded data for the prediction
A = future_environmental.drop("timestamp", axis=1)
A = A.drop("latitude", axis=1)
A = A.drop("longitude", axis=1)
# Predict
B = rf.predict(A)

# Add fire_risk to environmental data
future_environmental["fire_risk"] = B

#print(future_environmental)
future_environmental.to_csv("Future_Predicted.csv")
# Get only risks
fire_risk = future_environmental[future_environmental["fire_risk"] == 1]

print(fire_risk)
fire_risk.to_csv("Fire_Risks.csv")

# Folium
location_df = fire_risk.filter(["latitude", "longitude"], axis=1)
# Create a list to store all of the location data
location_list = location_df.values.tolist()
#print(location_list)

# initialize the map and store it in a m object
my_map = folium.Map(location = [44.2365, -72.1486], zoom_start = 4)
for lat, lon in location_list:
    popup_text = f"<br>Latitude: {lat}<br>Longitude: {lon}"
    folium.Marker([lat, lon], popup=popup_text).add_to(my_map)
# show the map
my_map.save('my_map.html')

