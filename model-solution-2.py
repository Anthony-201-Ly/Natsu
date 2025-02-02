# For AI Model Training https://youtu.be/29ZQ3TDGgRQ?si=D72UOyhjeHQdENxY
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

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

# Split dataframe into X and y
y = historical_fire_risk["fire_risk"]
print(y)

# Drop the fire_risk, timestamp, latitude, and longitude
X = historical_fire_risk.drop("fire_risk", axis=1)
X = X.drop("timestamp", axis=1)
X = X.drop("latitude", axis=1)
X = X.drop("longitude", axis=1)
print(X)

### Training the model
# Randomly choose 20% of the dataset to be used as test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

# We chose Random Forest Regression model
# due to having to having many independant variables
# as well as having numerical values for the dependant variable (Y "whether it will be a wildfire")
# being numerical/quantitative values rather than categorical values
rf = RandomForestRegressor(max_depth=2, random_state=100)
rf.fit(X_train, y_train)

# Applying the model to make a prediction on the test data
y_rf_train_pred = rf.predict(X_train)
y_rf_test_pred = rf.predict(X_test)

rf_train_mse = mean_squared_error(y_train, y_rf_train_pred)
rf_train_r2 = r2_score(y_train, y_rf_train_pred)

rf_test_mse = mean_squared_error(y_test, y_rf_test_pred)
rf_test_r2 = r2_score(y_test, y_rf_test_pred)

rf_results = pd.DataFrame(['Random forest', rf_train_mse, rf_train_r2, rf_test_mse, rf_test_r2]).transpose()
rf_results.columns = ['Method', 'Training MSE', 'Training R2', 'Test MSE', 'Test R2']
rf_results

print(rf_results)

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
# Get only risks
fire_risk = future_environmental[future_environmental["fire_risk"] == 1]

print(fire_risk)
# Empty DataFrame wtf?
