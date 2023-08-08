import streamlit as st
import os
import sys
from PIL import Image
from nutri_coach_repo.pages.User_Information import *
from nutri_coach_repo.prevmeal_analysis import *

# rootpath = os.path.join(os.getcwd(), '..')
# sys.path.append(rootpath)

analyze_img = Image.open("analyze.jpg")
st.image(analyze_img, width= 700)

st.title('Analyze Meals')

with st.container():
    meal_type = st.selectbox("Which meal do you want to analyze?", ('breakfast', 'lunch', 'dinner'))
    meal_title = st.text_input("What did you have?")
    quantity_metric = st.selectbox("Quantity metric", ('grams', 'servings'))
    quantity_value = st.number_input("Quantity value")

analyze_meal = st.button('Analyze the meal', use_container_width =True)

if analyze_meal:
    meal_analysis = analyze_prev_meal(meal_title,quantity_value, quantity_metric, age, gender, medical_condition)

    meal_quantity = meal_analysis[0]
    meal_calories = meal_analysis[1]
    meal_macros_grams = meal_analysis[2]
    meal_macros_perc = meal_analysis[3]
    meal_micros = meal_analysis[4]
    meal_benefits = meal_analysis[5]

    with st.container():
        mq = st.text_area(label='Quantity', value=meal_quantity, height=200)
        mcal = st.text_area(label='Calories', value=meal_calories, height=200)
        mac_gm = st.text_area(label='Macros in grams', value=meal_macros_grams, height=200)
        mac_perc = st.text_area(label='Macros in Percentage', value=meal_macros_perc, height=200)
        mic = st.text_area(label='Micro nutrients description', value=meal_micros, height=400)
        m_ben = st.text_area(label='Benefits', value=meal_benefits, height=400)
