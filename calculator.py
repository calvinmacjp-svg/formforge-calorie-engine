import math

# =========================
# 1. BMR (Base Metabolic Rate)
# =========================
def calculate_bmr(weight, height, age, gender):
    if gender.lower() == "male":
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161


# =========================
# 2. Activity System
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


def calculate_tdee(bmr, activity_level):
    return bmr * activity_multiplier(activity_level)


# =========================
# 3. Goal Engine
# =========================
def adjust_calories(tdee, goal):
    if goal == "lose weight":
        return tdee - 400
    elif goal == "gain muscle":
        return tdee + 300
    return tdee


# =========================
# 4. Macro Engine
# =========================
def calculate_macros(weight, calories):
    protein = weight * 2.2
    fats = weight * 0.9

    protein_cal = protein * 4
    fat_cal = fats * 9

    carbs = (calories - (protein_cal + fat_cal)) / 4

    return {
        "protein": round(protein),
        "carbs": round(max(carbs, 0)),
        "fats": round(fats)
    }


# =========================
# 5. Adaptive Transformation Engine
# =========================
def adaptive_rate(goal, activity, training_days):
    base = 0.4 if goal == "gain muscle" else 0.5

    if activity == "sedentary":
        base *= 0.85
    elif activity == "very active":
        base *= 1.1

    if training_days >= 5:
        base *= 1.1

    return round(min(base, 0.6), 2)


# =========================
# 6. Timeline Engine
# =========================
def estimate_timeline(weight_change, weekly_rate):
    if weekly_rate == 0:
        return 0
    return math.ceil(weight_change / weekly_rate)
