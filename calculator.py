import math

# =========================
# 1. BMR (Metabolic Base)
# =========================
def calculate_bmr(weight, height, age, gender):
    if gender.lower() == "male":
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161


# =========================
# 2. Activity Multiplier
# =========================
def activity_multiplier(level):
    levels = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725,
        "very active": 1.9
    }
    return levels.get(level.lower(), 1.55)


# =========================
# 3. TDEE (Maintenance Calories)
# =========================
def calculate_tdee(bmr, activity_level):
    return bmr * activity_multiplier(activity_level)


# =========================
# 4. Goal Adjustment System
# =========================
def adjust_calories(tdee, goal):
    if goal == "lose weight":
        return tdee - 400
    elif goal == "gain muscle":
        return tdee + 300
    else:
        return tdee


# =========================
# 5. Macro Engine (High Protein Priority)
# =========================
def calculate_macros(weight, calories):
    protein = weight * 2.2  # transformation driver
    fats = weight * 0.9     # hormonal support

    protein_cal = protein * 4
    fat_cal = fats * 9

    carbs_cal = calories - (protein_cal + fat_cal)
    carbs = carbs_cal / 4 if carbs_cal > 0 else 0

    return {
        "protein": round(protein),
        "carbs": round(carbs),
        "fats": round(fats)
    }


# =========================
# 6. Transformation Engine
# =========================
def weekly_progress(goal, target_change):
    if goal == "lose weight":
        return min(round(target_change / 0.5, 1), 1.0)
    elif goal == "gain muscle":
        return min(round(target_change / 0.25, 1), 0.5)
    return 0


# =========================
# 7. Timeline Estimator
# =========================
def estimate_timeline(weekly_rate, target_change):
    if weekly_rate == 0:
        return 0
    return math.ceil(target_change / weekly_rate)
