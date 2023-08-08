import streamlit as st
import os
import sys
from PIL import Image

from nutri_coach_repo.pages.User_Information import *
from nutri_coach_repo.meal_recipie_prompt_engg import generate_meal_plan

rootpath = os.path.join(os.getcwd(), '..')
sys.path.append(rootpath)

#User input from prev stage
# age = age
# gender = gender
# weight = weight
# height = height
# medical_condition= medical_condition
# dietary_pref= dietary_pref
# dislikes = dislikes

food = Image.open("food.jpg")
st.image(food, width= 600)

st.title('Plan A Meal')

with st.container():
    meal_of_the_day = st.selectbox("Which meal do you want to plan?", ('breakfast', 'lunch', 'dinner'))
    cuisine = st.text_input("Cuisine")
    ingredients = st.text_input("Enter the Ingredients in your pantry")

generate_meal = st.button('Generate meal plan', use_container_width =True)
if generate_meal:
    # inputs
    calorie_per_meal = cal_per_meal
    calorie_per_snack = cal_per_snack
    health_goal = goal
    macro_nutrient_distribution = macros

    meal_plan = generate_meal_plan(age,gender,medical_condition,dietary_pref, dislikes,calorie_per_meal,
                                   health_goal,cuisine, macro_nutrient_distribution, ingredients, meal_of_the_day)
    meal = meal_plan["meal"]
    meal_desc = meal_plan["meal_desc"]
    meal_micros = meal_plan["meal_micros"]
    meal_benefits = meal_plan["meal_benefits"]

    with st.container():
        m1= st.text_area(label = 'Recipe', value =meal, height= 800)
        m2 = st.text_area(label = 'Maco nutrients description', value = meal_desc, height= 400)
        m3 = st.text_area(label='Micro nutrients description', value= meal_micros, height=400)
        m4 = st.text_area(label='Benefits', value=meal_benefits, height=400)






