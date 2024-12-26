import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib

# Load dataset
data = pd.read_csv('traffic_data.csv')  # Replace with your dataset path

# Clean column names in case there are extra spaces
data.columns = data.columns.str.strip()

# Convert 'date_time' to datetime format
data['date_time'] = pd.to_datetime(data['date_time'])

# Extract features from 'date_time'
data['hour'] = data['date_time'].dt.hour
data['day_of_week'] = data['date_time'].dt.dayofweek
data['month'] = data['date_time'].dt.month

# Check if 'weather_main' column exists and map to numeric values if necessary
if 'weather_main' in data.columns:
    data['weather_main'] = data['weather_main'].map({'Clear': 0, 'Cloudy': 1, 'Rainy': 2})
else:
    print("Weather column 'weather_main' not found in the dataset.")

# Define the features and target column
features = ['hour', 'day_of_week', 'month', 'temperature', 'weather_main']
target = 'traffic_volume'

# Check if 'temperature' column exists
if 'temperature' not in data.columns:
    print("Warning: 'temperature' column is missing from the dataset. Proceeding without it.")
    features.remove('temperature')  # Remove 'temperature' from features list

# Ensure all necessary features are present in the dataset
missing_features = [feature for feature in features if feature not in data.columns]
if missing_features:
    print(f"Missing features: {missing_features}")
else:
    X = data[features]
    y = data[target]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the RandomForestRegressor
    model = RandomForestRegressor(n_estimators=100, random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Calculate Mean Absolute Error and Root Mean Squared Error
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    print(f"Mean Absolute Error: {mae}")
    print(f"Root Mean Squared Error: {rmse}")

    # Save the trained model to a .pkl file
    joblib.dump(model, 'traffic_volume_predictor.pkl')
