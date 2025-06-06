import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("brainrot_model.pkl")

st.title("🧠 BrainRot: Social Media Addiction Detector")
st.markdown("*Predict if you're addicted to social media based on your behavior.*")

# Input fields
screen_time = st.slider("Daily Screen Time (hours)", 0.0, 24.0, 5.0)
checks_per_hour = st.slider("Phone Checks per Hour", 0, 50, 10)
mood_swings = st.selectbox("Mood Swings without Social Media?", ["No", "Yes"])
sleeps_less = st.selectbox("Has Sleep Reduced?", ["No", "Yes"])
anxiety_level = st.slider("Anxiety Level (1 = Low, 5 = High)", 1, 5, 3)

# Convert to numeric
mood_swings = 1 if mood_swings == "Yes" else 0
sleeps_less = 1 if sleeps_less == "Yes" else 0

# Button
if st.button("Check Addiction"):
    input_data = np.array([[screen_time, checks_per_hour, mood_swings, sleeps_less, anxiety_level]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("🔴 You might be ADDICTED to social media. Time to detox 🧠📵")
    else:
        st.success("🟢 You're in control. Keep it that way! 🚀")

st.markdown("---")
st.caption("Project by Taruni – Powered by ML")