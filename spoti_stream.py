import streamlit as st
import pandas as pd

df = pd.read_csv('01 Spotify.csv')

df_plot = df[df['Stream']>100000000] 

st.write(df_plot)

st.write(len(df_plot))
