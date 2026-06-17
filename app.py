import streamlit as st
from calculator import *

st.set_page_config(page_title="FormForge Calorie Engine", layout="centered")

st.title("FormForge Calorie Engine")
st.caption("Personal Transformation System")

# ---------- INPUT FLOW ----------
goal = st.selectbox("What is your goal?", ["lose weight", "maintain", "gain muscle"])

target_change = 0
if goal != "maintain":
    target_change = st.number_input("How much weight change do you want (kg)?", min_value=0.0)

age = st.number_input("Age", min_value=10, max_value=100)
gender = st.selectbox("Gender", ["male", "female"])
height = st.number_input("Height (cm)", min_value=100, max_value=250)
weight = st.number_input("Weight (kg)", min_value=30, max_value=200)

activity = st.selectbox(
    "Activity Level",
    ["sedentary", "light", "moderate", "active", "very active"]
)

training_days = st.slider("Training days per week", 1, 7, 4)

# ---------- CALCULATION ----------
if st.button("Generate Plan"):

    bmr = calculate_bmr(weight, height, age, gender)
    tdee = calculate_tdee(bmr, activity)
    calories = adjust_calories(tdee, goal, target_change)

    macros = calculate_macros(weight, calories)

    weekly = weekly_progress(goal, target_change)
    weeks = estimate_timeline(target_change) if goal != "maintain" else 0

    # ---------- OUTPUT ----------
    st.subheader("Daily Targets")

    st.metric("Calories", f"{int(calories)} kcal")
    st.metric("Protein", f"{macros['protein']} g")
    st.metric("Carbs", f"{macros['carbs']} g")
    st.metric("Fats", f"{macros['fats']} g")

    st.subheader("Transformation Insight")

    if goal != "maintain":
        st.write(f"Estimated weekly change: {weekly} kg/week")
        st.write(f"Estimated timeline: {weeks} weeks")

    st.write("Training recommendation: 3–5 workouts per week minimum")
    st.write("Rule: Stay within ±5% of calorie target daily")

    # ---------- SIMPLE PROGRESS GRAPH ----------
    if goal != "maintain":
        import pandas as pd
        import numpy as np

        weeks_range = np.arange(0, weeks + 1)
        start_weight = weight

        if goal == "lose weight":
            weights = start_weight - (weeks_range * weekly)
        else:
            weights = start_weight + (weeks_range * weekly)

        df = pd.DataFrame({
            "Week": weeks_range,
            "Weight": weights
        })

        st.line_chart(df.set_index("Week"))
