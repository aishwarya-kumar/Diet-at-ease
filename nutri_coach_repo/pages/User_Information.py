import streamlit as st
import os
import sys
from PIL import Image
from streamlit_extras.metric_cards import style_metric_cards
rootpath = os.path.join(os.getcwd(), '..')
sys.path.append(rootpath)
from nutri_coach_repo.calorie_calculations import *

# Title
st.title('User Information')
st.divider()

# Container for user info
with st.container():
    user_img = Image.open('User_image.jpg')
    st.image(user_img, width=250)
    user_name = st.text_input('User Name')

    st.write("Basic Information")
    col1, col2 = st.columns(2)

    age = col1.number_input('Age', key="age")
    gender = col1.selectbox('Gender', ('F', 'M'), key="gender")
    weight = col1.number_input("Weight in KGs", key="weight")
    height = col1.number_input("Height in cms", key="height")
    medical_condition = col2.selectbox('Select metabolic disease',
                                       ('Diabetes', 'Obesity', 'Hypertension', 'High cholesterol'),
                                       key="medical_condition")
    activity_level = col2.selectbox('Activity level', ("Sedentary", "Lightly active", "Moderately active",
                                                       "Very active", "Extremely active"), key="activity_level")
    dietary_pref = col2.selectbox('Dietary preference', ("Vegetarian", "Vegan", "Eggetarian", "Gluten free",
                                                         "Lactose intolerant", "Non-Vegetarian"), key="dietary_pref")
    dislikes = col2.text_input("Food allergies/ dislikes", key="dislikes")

st.divider()

if age and gender and height and weight and medical_condition and dislikes and dietary_pref and activity_level:
    bmi_info = bmi_calc(height, weight, gender)
    goal = bmi_info[2]
    # print(bmi_info)

    TDEE = tdee_calc(gender, age, activity_level, weight, height)

    cals = calories_to_consume(TDEE, goal, gender)
    cal_per_meal = cals[0]
    # cal_per_snack = cals[1]

    macros = calc_macros(goal)

    if 'cal_per_meal' not in st.session_state:
        st.session_state['cal_per_meal'] = cals[0]

    if 'goal' not in st.session_state:
        st.session_state['goal'] = goal

    if 'macros' not in st.session_state:
        st.session_state['macros'] = macros

    # Derived inputs
    calorie_per_meal = cal_per_meal
    # calorie_per_snack = cal_per_snack
    health_goal = goal
    macro_nutrient_distribution = macros

    generate_info = st.button('Analyze BMI', use_container_width=True)
    if generate_info:

        st.write("Here is your BMI information based on your data:")
        col1, col2 = st.columns(2)
        col1.metric(label="BMI", value=bmi_info[0])
        col2.metric(label="Interpretation", value=bmi_info[1])
        col3, col4 = st.columns(2)
        col3.metric(label="Health goal", value=bmi_info[2])
        col4.metric(label="Calories per meal", value=cal_per_meal)
        style_metric_cards()