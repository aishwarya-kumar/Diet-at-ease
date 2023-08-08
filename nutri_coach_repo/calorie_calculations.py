# Functions for all calorie calculations
def bmi_calc(height, weight, gender):
    bmi = round(float(weight / (height*height))*10000.00, 1)
    
    if bmi <= 18.4:
        bmi_interpretation = "Underweight"
        goal = "weight_gain"
    elif (bmi >= 18.5) and (bmi <= 24.9):
        bmi_interpretation = "Normal"
        goal = "maintain_weight"
    elif (bmi >= 25.0) and (bmi <= 29.9):
        bmi_interpretation = "Overweight"
        goal = "weight_loss"
    elif bmi >= 30.0:
        bmi_interpretation = "Obesity"
        goal = "strict_weight_loss"
    else:
        print("Error: bmi out of bounds")
        
    return bmi, bmi_interpretation, goal


def tdee_calc(gender, age, activity_level, weight, height):
    
    if gender == 'M':
        BMR = 88.362 + (13.397 * weight) + (4.799 * height)- (5.677 * age)
    elif gender == 'F':
        BMR = 447.593 + (9.247 * weight) + (3.098 * height)- (4.330 * age)
        
    if activity_level == "Sedentary":
        tdee = round(BMR * 1.2, 0)
    elif activity_level == "Lightly active":
        tdee = round(BMR * 1.375, 0)
    elif activity_level == "Moderately active":
        tdee = round(BMR * 1.55, 0)
    elif activity_level == "Very active":
        tdee = round(BMR * 1.725, 0)
    elif activity_level == "Extremely active":
        tdee = round(BMR * 1.9, 0)
        
    return tdee
   

def calories_to_consume(tdee, goal, gender):
#     tdee = tdee_calc()
#     goal = bmi_calc()[2]

    if goal == "weight_gain":
        cals = tdee + 500
    elif goal == "maintain_weight":
        cals = tdee
    elif goal == "weight_loss":
        cals = tdee-500
    elif goal == "strict_weight_loss":
        cals = tdee-1000

    # If calories to be burnt is resulting in more less than min calories req per day then replace with floor value
    if gender == "F" and cals < 1200:
        cals = 1200
    elif gender == "M" and cals < 1500:
        cals = 1500
        
    cal_per_meal = cals/4
    
    cal_per_snack = cal_per_meal/2

    return cal_per_meal, cal_per_snack   


def calc_macros(goal):
    if goal == "weight_gain":
        carb_min = 0.5
        carb_max = 0.6
        protein_min = 0.1
        protein_max = 0.2
        fat_min = 0.2
        fat_max = 0.3

    elif goal == "maintain_weight":
        carb_min = 0.4
        carb_max = 0.4
        protein_min = 0.3
        protein_max = 0.3
        fat_min = 0.3
        fat_max = 0.3

    elif goal == "weight_loss" or "strict_weight_loss":
        carb_min = 0.4
        carb_max = 0.4
        protein_min = 0.3
        protein_max = 0.4
        fat_min = 0.2
        fat_max = 0.3

    macros = {'carb_min': carb_min, 'carb_max': carb_max, 'protein_min': protein_min,
              'protein_max': protein_max, 'fat_min': fat_min, 'fat_max': fat_max}
    return macros


def meal_of_the_day_analysis(meal_of_the_day, cal_per_meal, cals_consumed, macros_consumed, macros):
    if meal_of_the_day == "breakfast":
        meal_calories = cal_per_meal

    if meal_of_the_day == "lunch":
        if cals_consumed['bf_cals'] > cal_per_meal:
            print("Hey! You had a heavy breakfast today. I suggest you to have a healthy lunch")

        if macros_consumed['bf_carbs'] < macros['carb_min']:
            print("You had less carbs for breakfast")
            carb_min = macros['carb_min'] + 0.1
            carb_max = macros['carb_max'] + 0.1
        elif macros_consumed['bf_carbs'] > macros['carb_max']:
            print("You had more carbs for breakfast")
            carb_min = macros['carb_min'] - 0.1
            carb_max = macros['carb_max'] - 0.1

        if macros_consumed['bf_protein'] < macros['protein_min']:
            print("You had less proteins for breakfast")
            protein_min = macros['protein_min'] + 0.1
            protein_max = macros['protein_max'] + 0.1
        elif macros_consumed['bf_protein'] > macros['protein_max']:
            print("You had high proteins for breakfast")
            protein_min = macros['protein_min'] - 0.1
            protein_max = macros['protein_max'] - 0.1

        if macros_consumed['bf_fats'] < macros['fat_min']:
            print("You had less fats for breakfast")
            fat_min = macros['fat_min'] + 0.1
            fat_max = macros['fat_max'] + 0.1
        elif macros_consumed['bf_fats'] > macros['fat_max']:
            print("You had high fats for breakfast")
            fat_min = macros['fat_min'] - 0.1
            fat_max = macros['fat_max'] - 0.1

    if meal_of_the_day == "dinner":
        if cals_consumed['bf_cals'] + cals_consumed['lunch_cals'] > (2 * cal_per_meal):
            print("Hey! You had a heavy breakfast and lunch today. I suggest you to have a healthy and light dinner")

        if macros_consumed['bf_carbs'] + macros_consumed['lunch_carbs'] < macros['carb_min'] * 2:
            print("You had less carbs for breakfast and lunch")
            carb_min = macros['carb_min'] + 0.1
            carb_max = macros['carb_max'] + 0.1
        elif macros_consumed['bf_carbs'] + macros_consumed['lunch_carbs'] > macros['carb_max'] * 2:
            print("You had less carbs for breakfast and lunch")
            carb_min = macros['carb_min'] - 0.1
            carb_max = macros['carb_max'] - 0.1

        if macros_consumed['bf_protein'] + macros_consumed['lunch_protein'] < macros['protein_min'] * 2:
            print("You had less proteins for breakfast and lunch")
            protein_min = macros['protein_min'] + 0.1
            protein_max = macros['protein_max'] + 0.1
        elif macros_consumed['bf_protein'] + macros_consumed['lunch_protein'] > macros['protein_max'] * 2:
            print("You had high proteins for breakfast and lunch")
            protein_min = macros['protein_min'] - 0.1
            protein_max = macros['protein_max'] - 0.1

        if macros_consumed['bf_fats'] + macros_consumed['lunch_fats'] < macros['fat_min'] * 2:
            print("You had less fats for breakfast and lunch")
            fat_min = macros['fat_min'] + 0.1
            fat_max = macros['fat_max'] + 0.1
        elif macros_consumed['bf_fats'] + macros_consumed['lunch_fats'] > macros['fat_max'] * 2:
            print("You had high fats for breakfast and lunch")
            fat_min = macros['fat_min'] - 0.1
            fat_max = macros['fat_max'] - 0.1

    return carb_min, carb_max, protein_min, protein_max, fat_min, fat_max
