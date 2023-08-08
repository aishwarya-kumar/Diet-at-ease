import streamlit as st
import os
import sys
from PIL import Image
from streamlit_extras.metric_cards import style_metric_cards

from nutri_coach_repo.calorie_calculations import *
from nutri_coach_repo.pages.User_Information import *
from nutri_coach_repo.meal_recipie_prompt_engg import *

rootpath = os.path.join(os.getcwd(), '..')
sys.path.append(rootpath)

food = Image.open("food.jpg")
st.image(food, width= 600)

st.title('Plan A Meal')

with st.container():
    meal_of_the_day = st.selectbox("Which meal do you want to plan?", ('breakfast', 'lunch', 'dinner'))
    cuisine = st.text_input("Cuisine")
    ingredients = st.text_input("Enter the Ingredients in your pantry")


# age = age
# gender = gender
# weight = weight
# height = height
# medical_condition= medical_condition
# dietary_pref= dietary_pref
# dislikes = dislikes

calorie_per_meal= cal_per_meal
calorie_per_snack = cal_per_snack
health_goal = goal
macro_nutrient_distribution = macros

generate_meal = st.button('Generate meal plan', use_container_width =True)
if generate_meal:
    with st.container():
        m1= st.text_area(label = 'Recipe', value =meal, height= 1000)
        m2 = st.text_area(label = 'Maco nutrients description', value = meal_desc, height= 400)
        m3 = st.text_area(label='Micro nutrients description', value= meal_micros, height=400)
        m4 = st.text_area(label='Benefits', value=meal_benefits, height=400)






