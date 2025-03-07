import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('Ville on mahtava')


df = pd.read_csv('taajamat20112023.csv',sep=",")
st.write(df)


a = alt.Chart(df).mark_line().encode(
     x=alt.X('Vuosi',scale=alt.Scale(domain=[2010, 2025], clamp=True)),
     y=alt.Y('Väkiluku',scale=alt.Scale(domain=[50000, 400000], clamp=True)),
     color='Taajama'
     )

st.write(a)

b = alt.Chart(df).mark_line().encode(
     x=alt.X('Vuosi',scale=alt.Scale(domain=[2010, 2025], clamp=True)),
     y=alt.Y('Maapinta-ala_km2',scale=alt.Scale(domain=[10, 500], clamp=True)),
     color='Taajama'
     )

st.write(b)

c = alt.Chart(df).mark_line().encode(
     x=alt.X('Vuosi',scale=alt.Scale(domain=[2010, 2025], clamp=True)),
     y=alt.Y('Väestöntiheys',scale=alt.Scale(domain=[500, 2000], clamp=True)),
     color='Taajama'
     )

st.write(c)