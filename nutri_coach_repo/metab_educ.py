from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os
from secret_key import *

OPENAI_API = os.getenv('OPENAI_API_KEY')
chat = ChatOpenAI(temperature=0.0, openai_api_key=OPENAI_API)


# uses the LLM to generate facts
def generate_facts(metabolic_disorder):

    template_string = """Summarize the most useful facts about {metabolic_disorder} \
Format the output as JSON, where the keys are the question numbers"""

    prompt_template = ChatPromptTemplate.from_template(template_string)

    facts = prompt_template.format_messages(metabolic_disorder=metabolic_disorder)

    llm_facts = chat(facts)

    return llm_facts.content

# uses the LLM to generate questions using those facts
def generate_questions(metabolic_disorder, llm_facts):

    question_template = """\
For each fact listed about {metabolic_disorder}, generate one question that can be answered using only the information presented in that fact:

Format the output as JSON, where the keys are the question numbers

text: {text}
"""

    question_prompt_template = ChatPromptTemplate.from_template(question_template)

    questions = question_prompt_template.format_messages(metabolic_disorder=metabolic_disorder,
                                                     text = llm_facts)

    # Call the LLM to gather questions to ask the user
    list_of_questions = chat(questions)

    return list_of_questions.content

# use the LLM to assess user answer accuracy
def quiz_evaluation(user_provided_answers, metabolic_disorder, llm_facts):

    assessment_template = """\
Background information:
We're evaluating a set of user-provided answers, against a set of gold-truth answers.
We want to know if the user provided the correct answer. Output "CORRECT" if the user provided the correct answer.
Output "INCORRECT" if the user provided the incorrect answer.

Note: the user-provided answer and the gold-truth answer do not need to be written exactly the same in order for the
user-provided answer to be correct. We just want to assess if the user-provided answer GENERALLY matches what the
gold-truth answer is stating.


=========
For each fact listed about {metabolic_disorder}, Output "CORRECT" if the user provided the correct answer and \
output "INCORRECT" if the user provided the incorrect answer.

Format the output as JSON, where the keys are the question numbers

gold truth answers: {gold_truth}
user-provided answers: {user_provided}

"""

    assessment_prompt_template = ChatPromptTemplate.from_template(assessment_template)

    assessment = assessment_prompt_template.format_messages(metabolic_disorder=metabolic_disorder,
                                                     gold_truth = llm_facts,
                                                        user_provided = user_provided_answers)

     # Call the LLM to evaluate/assess the correctness of the user-provided answers.
    evaluations = chat(assessment)

    return evaluations.content

