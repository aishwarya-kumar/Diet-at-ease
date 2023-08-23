import streamlit as st
from PIL import Image
# from meal_recipie_prompt_engg import *
# from prevmeal_analysis import *
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.add_vertical_space import add_vertical_space


logo = Image.open('banner_images/DE logo.png')
st.image(logo, width=700)

st.title('Diet @ Ease')
st.divider()
st.subheader("Hey User! How are you doing today?")
st.divider()

with st.container():
   add_n_lines = 3
   add_vertical_space(add_n_lines)
   plan_meal = st.button('Plan a meal', use_container_width =True)
   add_vertical_space(add_n_lines)
   analyze_meal = st.button('Analyze a meal', use_container_width=True)
   add_vertical_space(add_n_lines)
   user_info = st.button('Edit user info', use_container_width=True)
   add_vertical_space(add_n_lines)
   nutri_edu = st.button('Nutritional Education', use_container_width=True)
   add_vertical_space(add_n_lines)
   meat_edu = st.button('Metabolic Education', use_container_width=True)

   if plan_meal:
      switch_page("Plan_a_meal")

   if analyze_meal:
      switch_page("Analyze_a_meal")

   if user_info:
      switch_page("User_Information")

   if nutri_edu:
      switch_page("Nutritional_Education")

   if meat_edu:
      switch_page("Metabolic_Education")







