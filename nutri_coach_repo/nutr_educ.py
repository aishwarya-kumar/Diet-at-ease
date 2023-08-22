"""

================================================================================================
================================================================================================
================================================================================================
|||||||||||||||||||||||||||   REMOVE API KEY BEFORE SENDING CODE   |||||||||||||||||||||||||||||
================================================================================================
================================================================================================
================================================================================================



"""

from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
import numpy as np
import os
import openai

from secret_key import *
OPENAI_API = os.getenv('OPENAI_API_KEY')
chat = ChatOpenAI(temperature=0.0, openai_api_key="")

# outputs a list of good foods (ones that would aid the user in managing their metabolic condition)
def good_foods_list(metabolic_disorder_val, num_foods_val):

    output_parser = CommaSeparatedListOutputParser()
    
    good_foods_template_string = """I have {metabolic_disorder} \
and I'm looking for expert nutritional guidance to help manage it effectively. \
Give me a list of {num_foods} foods and/or ingredients that would positively affect my ability to maintain my condition.\n{format_instructions}
"""

    format_instructions = output_parser.get_format_instructions()
    prompt = PromptTemplate(
        template=good_foods_template_string,
        input_variables=["metabolic_disorder", "num_foods"],
        partial_variables={"format_instructions": format_instructions}
    )

    model = OpenAI(temperature=0, openai_api_key="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")

    _input = prompt.format(metabolic_disorder=metabolic_disorder_val, num_foods=num_foods_val)
    output = model(_input)

    good_foods = output_parser.parse(output)

    return good_foods

# outputs a list of bad foods (ones that would NOT aid the user in managing their metabolic condition)
def bad_foods_list(metabolic_disorder_val, num_foods_val):
    output_parser = CommaSeparatedListOutputParser()

    bad_foods_template_string = """I have {metabolic_disorder} \
and I'm looking for expert nutritional guidance to help manage it effectively. \
Give me a list of {num_foods} foods and/or ingredients that would negatively affect my ability to maintain my condition.\n{format_instructions}
"""

    format_instructions = output_parser.get_format_instructions()
    prompt = PromptTemplate(
        template=bad_foods_template_string,
        input_variables=["metabolic_disorder", "num_foods"],
        partial_variables={"format_instructions": format_instructions}
    )

    model = OpenAI(temperature=0, openai_api_key="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")

    _input = prompt.format(metabolic_disorder=metabolic_disorder_val, num_foods=num_foods_val)
    output = model(_input)

    bad_foods = output_parser.parse(output)

    return bad_foods


# uses the good foods and bad foods list to generate a list of 3 questions to ask the user
# a seed is used after every shuffle, so that when the page refreshes (the foods items appear in the same questions,
#  and in the correct order)
def generate_questions(metabolic_disorder):

    # manually setting the number of foods generated to six
    good_foods = good_foods_list(metabolic_disorder, 6)
    bad_foods = bad_foods_list(metabolic_disorder, 6)

    sampled_good_foods_list = good_foods.copy()
    sampled_bad_foods_list = bad_foods.copy()
    np.random.seed(24)
    np.random.shuffle(sampled_good_foods_list)
    np.random.seed(24)
    np.random.shuffle(sampled_bad_foods_list)

    # each question will have one good food and two bad foods
    
    # used to track the answer choices per question
    # this will help in the evaluation step (assessing whether the user's answers are correct)
    foods_per_question_global = []

    # the string that will be used in the Streamlit UI text area
    str_for_text_area = ""

    # iterate to ask questions (manually setting the number of questions to ask to 3)
    for i in range(3):
        # print out the question
        # print("Question #", i+1)
        str_for_text_area = str_for_text_area + "Question #" + str(i+1) + "\n"
        # print("Which of the following foods can help you manage diabetes?")
        str_for_text_area =  str_for_text_area + "Which of the following foods can help you manage " \
            + metabolic_disorder + "?" + "\n-------------------------\n"

        # put the good food and bad foods into the list and shuffle the list
        foods = []
        good_food = sampled_good_foods_list.pop()
        foods.append(good_food)
        bad_food = sampled_bad_foods_list.pop()
        foods.append(bad_food)
        bad_food = sampled_bad_foods_list.pop()
        foods.append(bad_food)
        np.random.seed(24)
        np.random.shuffle(foods)
        foods_per_question_global.append(foods)

        # print("Option A: ", foods[0])
        str_for_text_area = str_for_text_area + "Option A: " + foods[0] + "\n"
        # print("Option B: ", foods[1])
        str_for_text_area = str_for_text_area + "Option B: " + foods[1] + "\n"
        # print("Option C: ", foods[2])
        str_for_text_area = str_for_text_area + "Option C: " + foods[2] + "\n"
        # print("\n")
        str_for_text_area = str_for_text_area + "\n"

    
    return str_for_text_area, foods_per_question_global, good_foods, bad_foods


# evaluates the user's answers
# food_items_per_question: a list of lists, each sublist contains the food items for that question #
# (index in sublist corresponds to that question number)
def eval_answers(food_items_per_question, question_number, answer, good_foods):

    if answer in good_foods and answer in food_items_per_question[question_number - 1]:
        return "Correct, you've selected the food that helps one manage diabetes"
    else:
        if answer not in food_items_per_question[question_number - 1]:
            return "Sorry, you've selected a food item that was not listed as an answer choice"
        else:
            return "Sorry, you've selected the incorrect answer choice"


