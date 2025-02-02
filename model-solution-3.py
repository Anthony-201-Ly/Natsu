# Reference For AI Model Training:  https://youtu.be/29ZQ3TDGgRQ?si=D72UOyhjeHQdENxY
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

historical_fire_risk = pd.read_csv("ProcessedData.csv")

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

# Applying the model to make a prediction
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