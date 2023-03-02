import streamlit
streamlit.title("My Moms's New Healthy Diner")
streamlit.header('Breakfast Favourites')
streamlit.text('🥣Omega3 and blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard boiled Free-Range Egg')
streamlit.text('🥑🍞Avacado taost')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
