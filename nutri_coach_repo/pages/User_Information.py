import streamlit as st
import os
import sys
from PIL import Image
from streamlit_extras.metric_cards import style_metric_cards

from nutri_coach_repo.calorie_calculations import *

rootpath = os.path.join(os.getcwd(), '..')
sys.path.append(rootpath)

#Title
st.title('User Information')
st.divider()

#Container for user info
with st.container():
    user_img = Image.open('User_image.jpg')
    st.image(user_img, width= 250)
    user_name = st.text_input('User Name')

    st.write("Basic Information")
    col1, col2 = st.columns(2)
    age = col1.number_input('Age')
    gender = col1.selectbox('Gender', ('F', 'M'))
    weight = col1.number_input("Weight in KGs")
    height= col1.number_input("Height in cms")

    medical_condition =col2.selectbox('Select metabolic disease', ('Diabetes', 'Obesity', 'Hypertension', 'High cholestrol'))
    activity_level = col2.selectbox('Activity level', ("Sedentary", "Lightly active", "Moderately active", "Very active", "Extremely active"))
    dietary_pref=  col2.selectbox('Activity level', ("Vegetarian", "Vegan","Eggitarian", "Gluten free", "Lactose intolerant", "Non-Vegetarian"))
    dislikes = col2.text_input("Food allergies/ dislikes")

st.divider()

# Calculations based on user input
# age = int(input("What is your age?"))
# gender = input("Enter gender")
# weight = int(input("Enter weight in kgs"))
# height = int(input("Enter height in cms"))
# medical_condition= input("Enter medical condition")
# activity_level = input("Enter activity level")
# dietary_pref= input("Enter Dietary preference")
# dislikes = input("Enter list of food you dislike/allergic to")

if age and gender and height and weight and medical_condition and dislikes and dietary_pref and activity_level:
    bmi_info = bmi_calc(height,weight, gender)
    goal = bmi_info[2]
    # print(bmi_info)

    TDEE= tdee_calc(gender, age, activity_level, weight, height)

    cals= calories_to_consume(TDEE, goal, gender)
    cal_per_meal = cals[0]
    cal_per_snack = cals[1]

    # print(cal_per_meal)
    # print(cal_per_snack)

    macros = calc_macros(goal)
    # print(macros)

    # Derived inputs
    calorie_per_meal= cal_per_meal
    calorie_per_snack = cal_per_snack
    health_goal = goal
    macro_nutrient_distribution = macros

# if age and gender and height and weight and medical_condition and dilikes and dietary_pref and activity_level:

generate_info = st.button('Analyze BMI', use_container_width =True)
if generate_info:
    st.write("Here is your BMI information based on your data:")
    col1, col2, col3 = st.columns(3)
    col1.metric(label="BMI", value=bmi_info[0])
    col2.metric(label="Interpretation", value=bmi_info[1])
    col3.metric(label="Health goal", value=bmi_info[2])
    style_metric_cards()

