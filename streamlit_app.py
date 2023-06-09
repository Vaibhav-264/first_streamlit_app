import streamlit
import pandas
streamlit.title('My parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
# fruit_list=ps.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list=my_fruit_list.set_index('Fruit')
# let's put a pick list here so they can pick a fruit they want to include 
streamlit.multiselect("Pick Some Fruits:",list(my_fruit_list.index))

# include fruit in the query itself and select that fruits
fruit_selected=streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
# display those fruit in table which is selected 
fruit_to_show=my_fruit_list.loc[fruit_selected]
# Display the table on the page
streamlit.dataframe(fruit_to_show)
