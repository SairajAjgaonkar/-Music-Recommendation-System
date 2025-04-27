# app.py
from recommender import collaborative_filtering, content_based_filtering
import streamlit as st


import pandas as pd

# Load the dataset first
df = pd.read_csv('gaanasongs.csv')
def eda(df):
    # Perform basic EDA
    top_singers = df['singer'].value_counts().head(10)
    return top_singers, None

# Now you can use df here safely


st.title('🎵 Music Recommendation System')

# Load & Preprocess Data



# Sidebar - EDA
st.sidebar.header('Exploratory Data Analysis')
if st.sidebar.checkbox('Show Top Singers'):
    top_singers, _ = eda(df)
    st.sidebar.write(top_singers)

if st.sidebar.checkbox('Show Language Distribution'):
    _, languages = eda(df)
    st.sidebar.write(languages)

# User Inputs
st.header('Find Songs You Might Like 🎧')
fav_singer = st.text_input('Enter your Favorite Singer:')
fav_language = st.text_input('Enter your Preferred Language:')

if st.button('Recommend by Singer'):
    if fav_singer:
        recs = collaborative_filtering(df, fav_singer)
        st.write('Here are some recommendations:')
        st.dataframe(recs)
    else:
        st.warning('Please enter a singer name.')

if st.button('Recommend by Language'):
    if fav_language:
        recs = content_based_filtering(df, fav_language)
        st.write('Here are some recommendations:')
        st.dataframe(recs)
    else:
        st.warning('Please enter a language.')
