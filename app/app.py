import streamlit as st
import joblib
import pandas as pd

st.title("🏠 House Price Predictor")

model = joblib.load("../model.pkl")

locality_options = [
    'BTM Layout',
    'Attibele',
    'K R Puram',
    'Marathahalli',
    'Indiranagar',
    'Electronic City',
    'Yalahanka',
    'Malleshwaram',
    'Jayanagar'
]
locality_options = sorted(locality_options)

facing_options = sorted([
    'North-West',
    'East',
    'North',
    'West',
    'North-East',
    'South-East',
    'South',
    'Missing'
])

parking_options = sorted([
    'Bike',
    'Bike and Car',
    'Car',
    'Missing'
])

with st.form("predict"):
    rent = st.number_input("Monthly Rent", value=15000)
    sqft = st.number_input("Square Feet", value=1000)
    locality = st.selectbox("Locality",locality_options,index=0)
    bedrooms = st.number_input("Bedrooms", value=2, min_value=0, max_value=10, step=1)
    bathrooms = st.number_input("Bathrooms", value=2, min_value=0, max_value=10, step=1)
    facing=st.selectbox("Facing",facing_options,index=0)
    parking = st.selectbox("Parking", parking_options,index=0)
    submitted = st.form_submit_button("Predict")

if submitted:
    X = pd.DataFrame([{
        "rent": rent,
        "area": sqft,
        "locality": locality if locality else "Missing",
        "BHK": bedrooms,
        "bathrooms": bathrooms,
        "facing":facing if facing else "Missing",
        "parking": parking if parking else "Missing"
    }])
    pred = model.predict(X)[0]
    st.success(f"Predicted Price: {pred:,.2f}")
