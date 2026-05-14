import streamlit as st
import requests

# -----------------------------
# Streamlit Page Config
# -----------------------------

st.set_page_config(
    page_title="Salary Prediction",
    page_icon="💼",
    layout="centered"
)

# -----------------------------
# Title
# -----------------------------

st.title("💼 Employee Salary Prediction")
st.write("Predict whether salary is <=50K or >50K")

# -----------------------------
# User Inputs
# -----------------------------

age = st.slider("Age", 21, 60, 30)

education = st.selectbox(
    "Education",
    ["Bachelors", "Masters", "PhD", "Diploma"]
)

hours_per_week = st.slider(
    "Hours Per Week",
    20,
    60,
    40
)

occupation = st.selectbox(
    "Occupation",
    ["Engineer", "Teacher", "Manager", "Developer", "Analyst"]
)

experience = st.slider(
    "Experience",
    1,
    35,
    5
)

# -----------------------------
# Prediction Button
# -----------------------------

if st.button("Predict Salary"):

    payload = {
        "age": age,
        "education": education,
        "hours_per_week": hours_per_week,
        "occupation": occupation,
        "experience": experience
    }

    response = requests.post(
        "http://fastapi:8000/predict",
        json=payload
    )

    result = response.json()

    st.write("API Response:", result)

    if response.status_code == 200 and "prediction" in result:
        st.success(f"Prediction: {result['prediction']}")
    else:
        st.error(f"API Error: {result}")
