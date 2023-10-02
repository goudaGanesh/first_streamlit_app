import streamlit
import pandas as pd
import requests
import json

streamlit.title('My Parents New Healthy Diner');

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.header('Breakfast Menu')
streamlit.text( '🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 🥑🍞Hard-Boiled Free-Range Egg')

# streamlit.dataframe(my_fruit_list);

streamlit.header('🥑🥑Build your own smoothie🥑🥑')

fruits_selected = streamlit.multiselect('Pick Some Fruits:',list(my_fruit_list.index),['Avocado','Strawberries']);
fruits_to_show = my_fruit_list.loc[fruits_selected]
#dispslay n 

streamlit.dataframe(fruits_to_show);
 
streamlit.header('Fruityvice Fruit Advice'); 
 # fruityvice api test
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())