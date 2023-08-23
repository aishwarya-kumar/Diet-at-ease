import streamlit as st
import os
import sys
from PIL import Image

rootpath = os.path.join(os.getcwd(), '..')
sys.path.append(rootpath)
from nutri_coach_repo.meal_recipie_prompt_engg import *

food = Image.open("banner_images/food.jpg")
st.image(food, width=700)

st.title('Plan A Meal')

with st.container():
    meal_of_the_day = st.selectbox("Which meal do you want to plan?", ('breakfast', 'lunch', 'dinner'), key="meal_of_the_day")
    cuisine = st.text_input("Cuisine")
    ingredients = st.text_input("Enter the Ingredients in your pantry")

calorie_per_meal = st.session_state['cal_per_meal']
# calorie_per_snack = cals[1]
health_goal = st.session_state['goal']
macro_nutrient_distribution = st.session_state['macros']

generate_meal = st.button('Generate meal plan', use_container_width=True)
if generate_meal:

    age = st.session_state['age']
    gender = st.session_state['gender']
    weight = st.session_state['weight']
    height = st.session_state['height']
    medical_condition = st.session_state['medical_condition']
    dietary_pref = st.session_state['dietary_pref']
    dislikes = st.session_state['dislikes']

    meal_plan = generate_meal_plan(age, gender, medical_condition, dietary_pref, dislikes, calorie_per_meal,
                                   health_goal, cuisine, macro_nutrient_distribution, ingredients, meal_of_the_day)
    meal = meal_plan[0]
    meal_desc = meal_plan[1]
    meal_micros = meal_plan[2]
    meal_benefits = meal_plan[3]

    with st.container():
        m1 = st.text_area(label='Recipe', value=meal, height=800)
        m2 = st.text_area(label='Maco nutrients description', value=meal_desc, height=400)
        m3 = st.text_area(label='Micro nutrients description', value=meal_micros, height=400)
        m4 = st.text_area(label='Benefits', value=meal_benefits, height=400)
