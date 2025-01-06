import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('windpower_model_compressed.pkl.gz')

# Define the input features for the user
st.title("Wind Power Prediction")

st.write("""
    This is an app to predict wind turbine power output based on wind speed, direction, and gusts.
""")

# User inputs (you can add more or modify as needed)
windspeed_10m = st.slider('Windspeed at 10m (m/s)', min_value=0.0, max_value=25.0, value=10.0, step=0.1)
windspeed_100m = st.slider('Windspeed at 100m (m/s)', min_value=0.0, max_value=25.0, value=12.0, step=0.1)
winddirection_10m = st.slider('Wind Direction at 10m (degrees)', min_value=0, max_value=360, value=180, step=1)
winddirection_100m = st.slider('Wind Direction at 100m (degrees)', min_value=0, max_value=360, value=180, step=1)
windgusts_10m = st.slider('Wind Gusts at 10m (m/s)', min_value=0.0, max_value=40.0, value=15.0, step=0.1)

# Convert the inputs into a DataFrame
input_data = pd.DataFrame({
    'windspeed_10m': [windspeed_10m],
    'windspeed_100m': [windspeed_100m],
    'winddirection_10m': [winddirection_10m],
    'winddirection_100m': [winddirection_100m],
    'windgusts_10m': [windgusts_10m]
})

# Prediction
if st.button("Predict Power Output"):
    prediction = model.predict(input_data)
    
    # Show the prediction result
    st.write(f"The predicted Wind Power Output is:\n {prediction[0]:.2f} (normalized between 0 and 1)")

