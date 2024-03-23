import streamlit as st
import pandas as pd
import numpy as np

st.write('lets go streamlit!')
name = st.text_input('Fill in your name:')
st.write('name entered is :', name)

st.write('## CSV exploration')
table = pd.read_csv("copper.csv")
st.write(table)

st.write("## Graphs and plots")

chart_data = pd.DataFrame(np.random.randn(20,3), columns = ['X Value','Y Value','Z Value'])
x = chart_data['X Value']
y = chart_data['Y Value']

# Line plot 
st.subheader('Line Plot')
st.line_chart(chart_data)
#bar chart
st.subheader('Bar Plot')
st.bar_chart(chart_data)

