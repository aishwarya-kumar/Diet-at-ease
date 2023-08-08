from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from pages.Analyze_a_meal import *

import os
from dotenv import load_dotenv
load_dotenv()


OPENAI_API = os.getenv('OPENAI_API_KEY')
llm = OpenAI(openai_api_key=OPENAI_API, temperature=0.9)

# User input
# meal_type = 'breakfast'
# meal_title = 'Paneer tikka'
# quantity_metric = 'servings'
# quantity_value = 1.5


def analyze_prev_meal(meal_title,quantity_value, quantity_metric, age, gender, medical_condition):

    # Templates
    meal_quantity_template = """ You need to analyze the quantity of this meal - {meal_title}.
    Meal name -  {meal_title} 
    Meal quantity - {quantity_value} {quantity_metric}
    
    If the quantity input is already provided in grams, print the quantity.
    If the quanity input is not provided in grams, estimate the quanitity of this meal - {meal_title} in grams. 
    Print the meal quantity.
    """

    meal_calories_template = """ You need to analyze the calories in this meal by understanding the {meal_title} and it's 
    quantity. 
    
    Meal name -  {meal_title} 
    Meal quantity - {quantity_value} {quantity_metric}
    
    Provide the total calories in thsi meal.
    """

    meal_macros_grams_template = """ You need to analyze the breakdown of the macronutrients in this meal 
    by understanding the {meal_title} and it's quantity. 
    
    Meal name -  {meal_title} 
    Meal quantity - {quantity_value} {quantity_metric}
    
    Provide a breakdown of the macronutrients carbohydrates, protiens and fats in grams. 
    """

    meal_macros_perc_template = """ You need to analyze the breakdown of the macronutrients in this meal 
    by understanding the {meal_title} and it's quantity. 
    
    Meal name -  {meal_title} 
    Meal quantity - {quantity_value} {quantity_metric}
    
    Provide a breakdown of percentage of  carbohydrates, protiens and fats. 
    """

    meal_micronutrients_template = """ You need to provide a description of all the micro nutrients, that is fibre, vitamins, 
    minerals and antioxidants present in the {meal_title}. No need to provide the amount it is present in. 
    Explain the health benefits of these micro nutrients. ONLY mention the micronutrients that are present in the {meal_title}, 
    you do not need to provide any explanation for the micronutrients that are not in {meal_title}.
    """

    meal_benefits_template = """ Explain how this meal -{meal_title} is healthy and how the ingridients are good for a 
    person of {age} years and  {gender} gender, who has the medical condition {medical_condition}.
    """

    # Prompts

    meal_quantity_template_prompt = PromptTemplate(
        template=meal_quantity_template,
        input_variables=['meal_title', 'quantity_value', 'quantity_metric']

    )

    meal_calories_template_prompt = PromptTemplate(
        template=meal_calories_template,
        input_variables=['meal_title', 'quantity_value', 'quantity_metric']

    )

    meal_macros_grams_template_prompt = PromptTemplate(
        template=meal_macros_grams_template,
        input_variables=['meal_title', 'quantity_value', 'quantity_metric']

    )

    meal_macros_perc_template_prompt = PromptTemplate(
        template=meal_macros_perc_template,
        input_variables=['meal_title', 'quantity_value', 'quantity_metric']

    )

    meal_micronutrients_template_prompt = PromptTemplate(
        template=meal_micronutrients_template,
        input_variables=['meal_title']
    )

    meal_benefits_template_prompt = PromptTemplate(
        template=meal_benefits_template,
        input_variables=['meal_title', 'age', 'gender', 'medical_condition']
    )

    # Chains

    meal_quantity_chain = LLMChain(
        llm=llm,
        prompt=meal_quantity_template_prompt,
        output_key="meal_quantity",
        verbose=True
    )

    meal_calories_chain = LLMChain(
        llm=llm,
        prompt=meal_calories_template_prompt,
        output_key="meal_calories",
        verbose=True
    )

    meal_macros_grams_chain = LLMChain(
        llm=llm,
        prompt=meal_macros_grams_template_prompt,
        output_key="meal_macros_grams",
        verbose=True
    )

    meal_macros_perc_chain = LLMChain(
        llm=llm,
        prompt=meal_macros_perc_template_prompt,
        output_key="meal_macros_perc",
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

    overall_chain_prevmeal = SequentialChain(
        chains=[meal_quantity_chain, meal_calories_chain, meal_macros_grams_chain, meal_macros_perc_chain,
                meal_micronutrients_chain, meal_benefits_chain],
        input_variables=['meal_title', 'quantity_value', 'quantity_metric', 'age', 'gender', 'medical_condition'],
        output_variables=["meal_quantity", "meal_calories", "meal_macros_grams", "meal_macros_perc",
                          "meal_micros", "meal_benefits"],
        verbose=True
    )

    output_prevmeal = overall_chain_prevmeal({'meal_title': meal_title, 'quantity_value': quantity_value,
                                              'quantity_metric': quantity_metric, 'age': age, 'gender': gender,
                                              'medical_condition': medical_condition})

    meal_quantity = output_prevmeal["meal_quantity"]
    meal_calories = output_prevmeal["meal_calories"]
    meal_macros_grams = output_prevmeal["meal_macros_grams"]
    meal_macros_perc = output_prevmeal["meal_macros_perc"]
    meal_micros = output_prevmeal["meal_micros"]
    meal_benefits = output_prevmeal["meal_benefits"]

    return meal_quantity, meal_calories, meal_macros_grams, meal_macros_perc, meal_micros, meal_benefits


