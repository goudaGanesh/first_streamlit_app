import streamlit
import pandas as pd
import requests
import json
import snowflake.connector
from urllib.error import URLError



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

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get(f"https://fruityvice.com/api/fruit/{this_fruit_choice}")
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json());
    return fruityvice_normalized
try:

    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
        streamlit.error("Please Select a fruit to get information")
    else:
        response = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(response)
    # streamlit.write(f'The user entered {fruit_choice}');

except:
    streamlit.error()

#normalising json response


# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
# my_data_rows = my_cur.fetchall()
streamlit.header("The Fruit Load List Contains:")
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute('SELECT * FROM FRUIT_LOAD_LIST')
        return my_cur.fetchall()


# add button
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)


streamlit.stop()

#new text box
new_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write(f'Thanks for adding {new_fruit}');

my_cur.execute(f"INSERT INTO FRUIT_LOAD_LIST VALUES('{new_fruit}')");