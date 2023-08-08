import streamlit as st
import os
import sys
from PIL import Image

from nutri_coach_repo.pages.User_Information import *
from nutri_coach_repo.pages.prevmeal_analysis import analyze_prev_meal

rootpath = os.path.join(os.getcwd(), '..')
sys.path.append(rootpath)

analyze_img = Image.open("analyze.jpg")
st.image(analyze_img, width= 800)

st.title('Analyze Meals')

with st.container():
    meal_type = st.selectbox("Which meal do you want to analyze?", ('breakfast', 'lunch', 'dinner'))
    meal_title = st.text_input("What did you have?")
    quantity_metric = st.selectbox("Quantity metric", ('grams', 'servings'))
    quantity_value = st.number_input("Quantity value")

analyze_meal = st.button('Analyze a plan', use_container_width =True)

if analyze_meal:
    meal_analysis = analyze_prev_meal(meal_title,quantity_value, quantity_metric, age, gender, medical_condition)

    meal_quantity = meal_analysis["meal_quantity"]
    meal_calories = meal_analysis["meal_calories"]
    meal_macros_grams = meal_analysis["meal_macros_grams"]
    meal_macros_perc = meal_analysis["meal_macros_perc"]
    meal_micros = meal_analysis["meal_micros"]
    meal_benefits = meal_analysis["meal_benefits"]

    