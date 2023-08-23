import streamlit as st
import os
import sys
from PIL import Image
import re

from nutri_coach_repo.metab_educ import *

# rootpath = os.path.join(os.getcwd(), '..')
# sys.path.append(rootpath)

analyze_img = Image.open("banner_images/analysisimage.jpg")
st.image(analyze_img, width= 700)

st.title('Metabolic Education')

# age = st.session_state['age']
# gender = st.session_state['gender']
# medical_condition = st.session_state['medical_condition']

with st.container():
    # meal_type = st.selectbox("Which meal do you want to analyze?", ('bf', 'lunch', 'dinner'))
    # meal_title = st.text_input("What did you have?")
    # quantity_metric = st.selectbox("Quantity metric", ('grams', 'servings'))
    # quantity_value = st.number_input("Quantity value")

    # Generate Facts
    original_metabolic_facts = generate_facts("diabetes")
    metabolic_facts = original_metabolic_facts[1:-1]
    metabolic_facts = metabolic_facts.strip()
    metabolic_facts = metabolic_facts.replace('"', '')
    metabolic_facts = metabolic_facts.replace(',\n  ', '\n')
    #metabolic_facts = metabolic_facts.replace(r"[0-9]+:", r"[0-9]\.", -1)
    #metabolic_facts = metabolic_facts.replace('\d:', '\d.')
    #metabolic_facts = re.sub(r"[0-9]+:", r"[0-9]+\.", metabolic_facts)
    txt = st.text_area('Here are some facts about diabetes', metabolic_facts,  height=800)

    # Generate Questions
    original_metabolic_questions = generate_questions("diabetes", metabolic_facts)
    metabolic_questions = original_metabolic_questions[1:-1]
    metabolic_questions = metabolic_questions.strip()
    metabolic_questions = metabolic_questions.replace('"', '')
    metabolic_questions = metabolic_questions.replace(',\n  ', '\n')
    # metabolic_questions = metabolic_questions.replace('\d:', '\d.')
    questions_txt = st.text_area('Answer the following the questions about diabetes', metabolic_questions,  height=800)

    # Quiz Evaluation
    user_answers = st.text_input("Enter your answers here:")
    if user_answers:
        eval_results = quiz_evaluation(user_answers, "diabetes", metabolic_facts)

        eval_results = eval_results[1:-1]
        eval_results = eval_results.strip()
        eval_results = eval_results.replace('"', '')
        eval_results = eval_results.replace(',\n  ', '\n')
        eval_results_txt = st.text_area('Quiz Results', eval_results,  height=800)

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
