import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib  # Assuming you want to load a pre-trained model

# Load pre-trained model
model = joblib.load('traffic_volume_predictor.pkl')  # Replace with the correct model path

# Streamlit UI
st.title("Traffic Volume Prediction")
st.write("Predict traffic volume based on input parameters.")

# Input fields for the model prediction
hour = st.slider("Hour of Day", 0, 23, 8)
day_of_week = st.selectbox("Day of Week", range(7))
month = st.selectbox("Month", range(1, 13))
temperature = st.number_input("Temperature (°C)", 0, 40)
weather = st.selectbox("Weather Condition", ['Clear', 'Cloudy', 'Rainy'])

# Map weather condition to numeric values for prediction
weather_mapping = {'Clear': 0, 'Cloudy': 1, 'Rainy': 2}
weather_num = weather_mapping.get(weather, -1)

# Predict when the button is clicked
if st.button("Predict"):
    if model:
        # Prepare input data for prediction
        # Ensure only the features that were used during training are passed (removing 'temperature' if needed)
        input_data = np.array([[hour, day_of_week, month, weather_num]])

        # Predict traffic volume
        prediction = model.predict(input_data)
        st.write(f"Predicted Traffic Volume: {int(prediction[0])} vehicles")
    else:
        st.error("Model is not trained or loaded correctly.")
