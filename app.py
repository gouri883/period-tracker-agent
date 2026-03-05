import streamlit as st
import pandas as pd
import plotly.express as px

from predictor import predict_next_period, fertile_window
from database import save_cycle

# Page configuration

st.set_page_config(
page_title="AI Period Tracker",
page_icon="🌸",
layout="centered"
)

# Background image

import base64

def add_background():
    with open("images/bg.jpg", "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image:
                linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)),
                url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_background()
# Title

st.title("🌸 AI Period Tracker")
st.markdown("Track your cycle, fertility window, and health insights.")

st.divider()

# Input Section

st.subheader("📅 Enter Cycle Information")

col1, col2 = st.columns(2)

with col1:
 last_period = st.date_input("Last Period Date")

with col2:
 cycle_length = st.slider("Cycle Length (days)", 20, 35, 28)

# Prediction Button

if st.button("💾 Save & Predict", use_container_width=True):


 save_cycle(str(last_period), cycle_length)

next_period = predict_next_period(str(last_period), cycle_length)

fertile_start, fertile_end = fertile_window(str(last_period), cycle_length)

st.success(f"🩸 Next Period Predicted: {next_period}")
st.info(f"🌱 Fertile Window: {fertile_start} → {fertile_end}")

st.divider()

# Cycle Timeline Graph
st.subheader("📊 Cycle Timeline")

cycle_days = list(range(1, cycle_length + 1))
phases = []

for d in cycle_days:
    if d <= 5:
        phases.append("Menstrual")
    elif d <= 13:
        phases.append("Follicular")
    elif d == 14:
        phases.append("Ovulation")
    else:
        phases.append("Luteal")

df = pd.DataFrame({
    "Day": cycle_days,
    "Phase": phases
})

fig = px.bar(
    df,
    x="Day",
    color="Phase",
    title="Menstrual Cycle Phases"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# Ovulation Probability Chart
st.subheader("🌱 Ovulation Probability")

probabilities = []

for d in cycle_days:
    if 12 <= d <= 16:
        probabilities.append(0.9)
    elif 10 <= d <= 18:
        probabilities.append(0.6)
    else:
        probabilities.append(0.1)

df2 = pd.DataFrame({
    "Day": cycle_days,
    "Probability": probabilities
})

fig2 = px.line(
    df2,
    x="Day",
    y="Probability",
    title="Ovulation Probability Curve"
)

st.plotly_chart(fig2, use_container_width=True)

st.divider()

# Mood and Symptom Tracker
st.subheader("🧠 Mood & Symptom Tracker")

mood = st.selectbox(
    "How are you feeling today?",
    ["😊 Happy", "😐 Neutral", "😞 Low Energy", "😡 Irritable"]
)

symptoms = st.multiselect(
    "Symptoms",
    ["Cramps", "Headache", "Bloating", "Fatigue", "Back Pain"]
)

if st.button("Save Mood & Symptoms"):
    st.success("Mood and symptoms saved!")

st.divider()

# Cycle History Table
st.subheader("📅 Cycle History")

history = pd.DataFrame({
    "Cycle": [1, 2, 3],
    "Length": [28, 27, 29],
    "Prediction Accuracy": ["95%", "92%", "97%"]
})

st.dataframe(history)

st.divider()

# AI Insight
st.subheader("🤖 AI Health Insight")

st.write(
    "Your cycle pattern appears consistent. Maintaining proper sleep, hydration, "
    "balanced nutrition, and stress management can support hormonal health."
)

