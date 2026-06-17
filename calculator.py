import math

# ---------- TDEE CALCULATION ----------
def calculate_bmr(weight, height, age, gender):
    # Mifflin-St Jeor Equation
    if gender.lower() == "male":
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161


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


# ---------- CALORIE ADJUSTMENT ----------
def adjust_calories(tdee, goal, target_change=0):
    if goal == "lose weight":
        return tdee - (300 + min(target_change * 50, 200))
    elif goal == "gain muscle":
        return tdee + (200 + min(target_change * 50, 200))
    else:
        return tdee


# ---------- MACROS ----------
def calculate_macros(weight, calories):
    protein = weight * 2.2  # high priority
    protein_cal = protein * 4

    fats = weight * 0.9
    fat_cal = fats * 9

    carbs_cal = calories - (protein_cal + fat_cal)
    carbs = carbs_cal / 4 if carbs_cal > 0 else 0

    return {
        "protein": round(protein),
        "carbs": round(carbs),
        "fats": round(fats)
    }


# ---------- PROJECTION ----------
def weekly_progress(goal, target_change):
    if goal == "lose weight":
        return round(target_change / 0.4, 1)  # avg fat loss/week
    elif goal == "gain muscle":
        return round(target_change / 0.25, 1)  # muscle gain rate
    return 0


def estimate_timeline(target_change):
    weeks = target_change / 0.4
    return math.ceil(weeks)
