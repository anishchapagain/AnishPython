import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
#import plotly.express as px
#https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py

st.title("Earthquake 2015")
st.write("""
# Analysing EarthQuake - 2015
- ***Seismonepal*** data to be interpreted.
""")
st.markdown("***")

#df=pd.read_csv('E:\\AnacondaPythonScripts\\Python_Tutorial\\PythonNotes\\requests_lxml_pandas\\earthquake.csv')
df=pd.read_csv('..\\requests_lxml_pandas\\earthquakeTest.csv')

st.write("Header Data --")
st.write(df.head(50))
st.markdown("***")
st.write("Footer Data --")
st.dataframe(df.tail(50))
st.write("Magnitude....")
st.line_chart(df['Magnitude'])
st.write("Magnitude: value_counts()....")
st.line_chart(df['Epicentre'].value_counts())

scaleKathmandu = df[(df['Epicentre']=='Dolakha') & (df.Magnitude>4)][['Magnitude','Date']]
scaleKathmandu = scaleKathmandu.sort_values(by='Date').set_index('Date')
#scaleKathmandu.plot(kind='bar')
st.bar_chart(scaleKathmandu)
st.markdown("***")

lat=df.Latitude
lon=df.Longitude
city=df.Epicentre
map_data = pd.DataFrame({'city':city,'lat':lat,'lon':lon})
st.map(map_data)
st.markdown("***")
"""
### By: Anish Chapagain
"""
