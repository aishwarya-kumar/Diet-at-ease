import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from pages.User_Information import *
from pages.Plan_a_meal import *

load_dotenv()

OPENAI_API = os.getenv('OPENAI_API_KEY')
llm = OpenAI(openai_api_key=OPENAI_API, temperature=0.9)

# User inputs:
# cuisine = input("Enter cuisine: ")
# ingredients = input("Enter list of ingredients: ")
# meal_of_the_day = input("Enter meal of the day: ")

# Prompt engineering


def generate_meal_plan(age, gender, medical_condition, dietary_pref, dislikes, calorie_per_meal, health_goal, cuisine,
                       macro_nutrient_distribution, ingredients, meal_of_the_day):
    # Templates:
    meal_recipie_template = """ You are a nutrition coach for users suffering from metabolic disorders like diabetes, 
    hypertension, high lipids or obesity. The users are generally below the age of 40. Your job is to understand the 
    user details and generate a meal plan for them based on the ingredients available in their pantry, 
    their dietary preference, cuisine of choice, calorie requirements to align with their overall health goal. 
    User details are given as follows:
    'age': {age}, 'gender' = {gender}, 'medical_condition' : {medical_condition}, 
    'dietary_pref':{dietary_pref}, 'dislikes': {dislikes}, 
    'calorie_per_meal' : {calorie_per_meal}, 'health_goal' :{health_goal},
    'cuisine': {cuisine}, 'macro_nutrient_distribution': {macro_nutrient_distribution}
    'ingredients': {ingredients}, meal_of_the_day = {meal_of_the_day}
    
    You do not give any medical advice, only generate recipies.
    You need to follow the dietary preference and cuisine VERY STRICTLY. 
    
    Consider their dislikes and try not adding these ingredients in the meals.
    Consider their health goal - the meal plan should be in accordance with it. 
    
    The meal should contain calories within the maximum amount provided.
    The split of macronutrients carbohydrates, proteins and fats needs to be based on the minimum and maximum 
    values given in {macro_nutrient_distribution}.
    
    The meal should be made out of the ingredients provided. 
    If any ingredients are missing, mention what additional ingredients are required to make the recipie.
    
    The meal needs to be real and edible. DO NOT invent new recipes.
    
    Generate ONE recipie based on the above requirements. Print the name of the recipie and detailed instructions to cook with 
    cooking time, ingredients required ad other necessary details. 
    """

    meal_description_template = """ You need to provide the calories in the generated meal: {meal} per one serving. Provide a 
    split of the macro nutrients carbohydrates, proteins and fats in the {meal} for one serving in weight. Provide the
    percentage contribution of each macronutrient to the meal, and the number of calories each macro nutrient is contributing to.
    """

    meal_micronutrients_template = """ You need to provide a description of all the micro nutrients, that is fibre, vitamins, 
    minerals and antioxidants present in the {meal}. No need to provide the amount it is present in. Explain the health benefits 
    of these micro nutrients.
    """

    meal_benefits_template = """ Explain how this {meal} is healthy and how the ingredients are good for a 
    person of {age} years and  {gender} gender, who has the medical condition {medical_condition}.
    """
    # Prompt Templates
    meal_recipie_template_prompt = PromptTemplate(
        template=meal_recipie_template,
        input_variables=['age', 'gender', 'medical_condition', 'dietary_pref', 'dislikes', 'calorie_per_meal', 'health_goal',
                         'cuisine', 'macro_nutrient_distribution', 'ingredients', 'meal_of_the_day']
    )

    meal_description_template_prompt = PromptTemplate(
        template=meal_description_template,
        input_variables=['meal']
    )

    meal_micronutrients_template_prompt = PromptTemplate(
        template=meal_micronutrients_template,
        input_variables=['meal']
    )

    meal_benefits_template_prompt = PromptTemplate(
        template=meal_benefits_template,
        input_variables=['meal', 'age', 'gender', 'medical_condition']
    )

    # LLM Chains
    meal_chain = LLMChain(
        llm=llm,
        prompt=meal_recipie_template_prompt,
        output_key="meal",
        verbose=True
    )

    meal_desc_chain = LLMChain(
        llm=llm,
        prompt=meal_description_template_prompt,
        output_key="meal_desc",
        verbose=True
    )

    meal_micronutrients_chain = LLMChain(
        llm=llm,
        prompt=meal_micronutrients_template_prompt,
        output_key="meal_micros",
        verbose=True
    )

    meal_benefits_chain = LLMChain(
        llm=llm,
        prompt=meal_benefits_template_prompt,
        output_key="meal_benefits",
        verbose=True
    )

    overall_chain = SequentialChain(
        chains=[meal_chain, meal_desc_chain, meal_micronutrients_chain, meal_benefits_chain],
        input_variables=['age', 'gender', 'medical_condition', 'dietary_pref', 'dislikes', 'calorie_per_meal', 'health_goal',
                         'cuisine', 'macro_nutrient_distribution', 'ingredients', 'meal_of_the_day'],
        output_variables=["meal", "meal_desc", "meal_micros", "meal_benefits"],
        verbose=True
    )

    output = overall_chain({'age': age, 'gender': gender, 'medical_condition': medical_condition,
                            'dietary_pref': dietary_pref, 'dislikes': dislikes, 'calorie_per_meal': calorie_per_meal,
                            'health_goal': health_goal, 'cuisine': cuisine,
                            'macro_nutrient_distribution': macro_nutrient_distribution, 'ingredients': ingredients,
                            'meal_of_the_day': meal_of_the_day})
    meal = output["meal"]
    meal_desc = output["meal_desc"]
    meal_micros = output["meal_micros"]
    meal_benefits = output["meal_benefits"]

    return meal, meal_desc, meal_micros, meal_benefits
