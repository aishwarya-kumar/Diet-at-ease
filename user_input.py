#Getting user input 

from calorie_calculations import *

age = int(input("What is your age?"))
gender = input("Enter gender")
weight = int(input("Enter weight in kgs"))
height = int(input("Enter height in cms"))
medical_condition= input("Enter medical condition")
activity_level = input("Enter activity level")
dietary_pref= input("Enter Dietary preference")
dislikes = input("Enter list of food you dislike/allergic to")


bmi_info = bmi_calc(height,weight, gender)
goal = bmi_info[2]
print(bmi_info)
print(goal)

TDEE= tdee_calc(gender, age, activity_level, weight, height)
print(TDEE)

cals= calories_to_consume(TDEE, goal, gender)
cal_per_meal = cals[0]
cal_per_snack = cals[1]

print(cal_per_meal)
print(cal_per_snack)

macros = calc_macros(goal)
print(macros)

# Derived inputs
calorie_per_meal= cal_per_meal
calorie_per_snack = cal_per_snack
health_goal = goal
macro_nutrient_distribution = macros



# User inputs:
# age = 28
# gender = "F"
# weight = 85
# height = 161
# medical_condition= "diabetes"
# activity_level = "sedentary"
# dietary_pref= "eggiterian"
# dislikes = "curd, yogurt,buttermilk, anchovies, asparagus, kale"
# cuisine = "Continental"
# ingridients = ["potato", "mushroom", "onion", "flour", "eggs"]
# meal_of_the_day = 'lunch'