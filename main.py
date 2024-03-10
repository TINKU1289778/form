import streamlit as st
import pandas as pd

a=pd.read_csv('Book1.csv')

st.dataframe(a)

st.markdown("""print("hello world")""")

st.text_input("enter your email")
st.text_input("enter your password for comform")