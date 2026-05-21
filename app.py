import streamlit as st
import pandas as pd

st.title("My Streamlit App")

df = pd.read_excel('Netflix_Entertainment_Dataset.xlsx')

st.dataframe(df)
