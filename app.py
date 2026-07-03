import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Performance Prediction")
st.write("Enter the student details below to predict the final grade (G3).")

# Input Fields
studytime = st.selectbox(
    "Study Time (1-4)",
    [1, 2, 3, 4]
)

failures = st.number_input(
    "Number of Past Failures",
    min_value=0,
    max_value=4,
    value=0
)

absences = st.number_input(
    "Absences",
    min_value=0,
    max_value=100,
    value=5
)

G1 = st.number_input(
    "First Period Grade (G1)",
    min_value=0,
    max_value=20,
    value=10
)

G2 = st.number_input(
    "Second Period Grade (G2)",
    min_value=0,
    max_value=20,
    value=10
)

# Prediction
if st.button("Predict Final Grade"):

    features = np.array([[studytime, failures, absences, G1, G2]])

    prediction = model.predict(features)

    st.success(f"Predicted Final Grade (G3): {prediction[0]:.2f}")

    if prediction >= 16:
        st.balloons()
        st.success("🌟 Excellent Performance")

    elif prediction >= 10:
        st.info("👍 Average Performance")

    else:
        st.error("📚 Needs Improvement")