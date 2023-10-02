import streamlit
import pandas as pd
import requests
import json
import snowflake.connector
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
 
  # fruityvice api 
streamlit.header('Fruityvice Fruit Advice'); 
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write(f'The user entered {fruit_choice}');

fruityvice_response = requests.get(f"https://fruityvice.com/api/fruit/{fruit_choice}");

#normalising json response
fruityvice_normalized = pd.json_normalize(fruityvice_response.json());
streamlit.dataframe(fruityvice_normalized);


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
my_data_row = my_cur.fetchone()
streamlit.header("The Fruit Load List Contains:")
streamlit.dataframe(my_data_row)