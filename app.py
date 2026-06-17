import streamlit as st
import pandas as pd
import numpy as np

from calculator import (
    calculate_bmr,
    calculate_tdee,
    adjust_calories,
    calculate_macros,
    weekly_progress,
    estimate_timeline
)

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="FormForge Engine", layout="centered")

st.title("FormForge Calorie Engine")
st.caption("Personal Transformation System")

st.markdown("---")


# =========================
# INPUTS
# =========================
goal = st.selectbox("What is your goal?", ["lose weight", "maintain", "gain muscle"])

target_change = 0
if goal != "maintain":
    target_change = st.number_input("How much weight change do you want (kg)?", min_value=0.0, value=5.0)

age = st.number_input("Age", min_value=10, max_value=100, value=20)
gender = st.selectbox("Gender", ["male", "female"])

height = st.number_input("Height (cm)", min_value=100, max_value=250, value=176)
weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=65)

activity = st.selectbox(
    "Activity Level",
    ["sedentary", "light", "moderate", "active", "very active"]
)

training_days = st.slider("Training days per week", 1, 7, 4)

st.markdown("---")


# =========================
# GENERATE BUTTON
# =========================
if st.button("Generate Transformation Plan"):

    # ---------- ENGINE CALCULATION ----------
    bmr = calculate_bmr(weight, height, age, gender)
    tdee = calculate_tdee(bmr, activity)
    calories = adjust_calories(tdee, goal)

    macros = calculate_macros(weight, calories)

    weekly = weekly_progress(goal, target_change)
    weeks = estimate_timeline(weekly, target_change) if goal != "maintain" else 0


    # =========================
    # DASHBOARD HEADER
    # =========================
    st.markdown("## 📊 FormForge Transformation Dashboard")
    st.markdown("---")


    # =========================
    # METRICS CARDS
    # =========================
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Calories", f"{int(calories)} kcal")

    with col2:
        st.metric("Protein", f"{macros['protein']} g")

    with col3:
        st.metric("Training", f"{training_days} days")


    st.markdown("---")


    # =========================
    # MACRO BREAKDOWN
    # =========================
    st.markdown("## 🧬 Macro System")

    st.write(f"Protein: {macros['protein']} g (Transformation Driver)")
    st.write(f"Carbs: {macros['carbs']} g (Energy Fuel)")
    st.write(f"Fats: {macros['fats']} g (Hormonal Stability)")

    st.markdown("---")


    # =========================
    # INTELLIGENCE LAYER
    # =========================
    st.markdown("## 🧠 Transformation Intelligence")

    if goal == "gain muscle":
        st.info("Lean mass accumulation mode activated. Protein prioritization engaged for hypertrophy optimization.")

    elif goal == "lose weight":
        st.info("Fat loss protocol active. Controlled deficit engaged for sustainable reduction while preserving muscle.")

    else:
        st.info("Maintenance mode active. Focus on performance stability and metabolic balance.")


    st.markdown("---")


    # =========================
    # PROJECTION ENGINE
    # =========================
    st.markdown("## 📈 Progress Projection")

    if goal != "maintain":
        st.write(f"Weekly Change Rate: {weekly} kg/week")
        st.write(f"Estimated Timeline: {weeks} weeks")


        # =========================
        # GRAPH SYSTEM
        # =========================
        weeks_range = np.arange(0, max(weeks, 1) + 1)
        start_weight = weight

        if goal == "lose weight":
            weights = start_weight - (weeks_range * weekly)
        else:
            weights = start_weight + (weeks_range * weekly)

        df = pd.DataFrame({
            "Week": weeks_range,
            "Projected Weight": weights
        })

        st.markdown("## 📉 Body Transformation Curve")
        st.line_chart(df.set_index("Week"))


    st.markdown("---")


    # =========================
    # ACTION SUMMARY
    # =========================
    st.markdown("## ⚡ Action Summary")

    st.write(f"Daily Calorie Target: {int(calories)} kcal")
    st.write(f"Protein Target: {macros['protein']} g")
    st.write("Rule: Stay within ±5% of calorie target daily")
    st.write("Training: Minimum 3–5 workouts per week recommended")
