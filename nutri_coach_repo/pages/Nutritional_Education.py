import streamlit as st
import os
import sys
from PIL import Image

from nutri_coach_repo.nutr_educ import *

analyze_img = Image.open("analysisimage.jpg")
st.image(analyze_img, width= 700)

st.title('Nutritional Education')

# age = st.session_state['age']
# gender = st.session_state['gender']
# medical_condition = st.session_state['medical_condition']

# checking to see if this number stays the same (prevents the refresh of questions)
static=100

nutritional_questions, foods_per_question, good_foods, bad_foods = generate_questions("diabetes")

with st.container():
    # meal_type = st.selectbox("Which meal do you want to analyze?", ('bf', 'lunch', 'dinner'))
    # meal_title = st.text_input("What did you have?")
    # quantity_metric = st.selectbox("Quantity metric", ('grams', 'servings'))
    # quantity_value = st.number_input("Quantity value")

    
    if static==100:
        questions_to_output = nutritional_questions
        foods_per_question_to_use = foods_per_question
        good_foods_to_use = good_foods
        bad_foods_to_use = bad_foods

    nutritional_questions_txt = st.text_area('Nutritional Questions', questions_to_output,  height=600)

    # Quiz Evaluation
    answer_1 = st.text_input("Enter your answer to Question #1.")
    if answer_1:
        results = eval_answers(foods_per_question_to_use, 1, answer_1, good_foods_to_use)
        eval_results_txt_1 = st.text_area('Question #1 Results', results)

    answer_2 = st.text_input("Enter your answer to Question #2.")
    if answer_2:
        results = eval_answers(foods_per_question_to_use, 2, answer_2, good_foods_to_use)
        eval_results_txt_2 = st.text_area('Question #2 Results', results)

    answer_3 = st.text_input("Enter your answer to Question #3.")
    if answer_3:
        results = eval_answers(foods_per_question_to_use, 3, answer_3, good_foods_to_use)
        eval_results_txt_3 = st.text_area('Question #3 Results', results)

    # ensures refresh will not change the page
    static += 1

# analyze_meal = st.button('Analyze the meal', use_container_width =True)

# if analyze_meal:
#     meal_analysis = analyze_prev_meal(meal_title,quantity_value, quantity_metric, age, gender, medical_condition)

#     meal_quantity = meal_analysis[0]
#     meal_calories = meal_analysis[1]
#     meal_macros_grams = meal_analysis[2]
#     meal_macros_perc = meal_analysis[3]
#     meal_micros = meal_analysis[4]
#     meal_benefits = meal_analysis[5]

#     with st.container():
#         mq = st.text_area(label='Quantity', value=meal_quantity, height=200)
#         mcal = st.text_area(label='Calories', value=meal_calories, height=200)
#         mac_gm = st.text_area(label='Macros in grams', value=meal_macros_grams, height=200)
#         mac_perc = st.text_area(label='Macros in Percentage', value=meal_macros_perc, height=200)
#         mic = st.text_area(label='Micro nutrients description', value=meal_micros, height=400)
#         m_ben = st.text_area(label='Benefits', value=meal_benefits, height=400)
