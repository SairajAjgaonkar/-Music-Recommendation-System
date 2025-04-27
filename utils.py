# utils.py

import pandas as pd

def load_data(path):
    df = pd.read_csv("C:\Users\sagar\Desktop\py\ML\Construct Week\gaanasongs.csv")
    return df

def preprocess_data(df):
    df = df.drop_duplicates(subset=['name', 'singer'])
    df.dropna(subset=['name', 'singer', 'duration', 'link', 'language'], inplace=True)
    df['duration'] = pd.to_numeric(df['duration'], errors='coerce')
    df.dropna(subset=['duration'], inplace=True)
    return df

def eda(df):
    top_singers = df['singer'].value_counts().head(10)
    languages = df['language'].value_counts()
    return top_singers, languages
