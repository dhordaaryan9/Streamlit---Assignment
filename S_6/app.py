import streamlit as st
import pandas as pd
import requests

st.title("Trending Movies App 🎬")
st.write("Welcome to the Trending Movies Tracker!")

# Dummy data for demonstration purposes as TMDB API would require an API key
dummy_movies = [
    {"title": "The Grand Space Adventure", "rating": 8.5, "genre": "Sci-Fi"},
    {"title": "Mystery in the Alps", "rating": 7.9, "genre": "Thriller"},
    {"title": "Love in Paris", "rating": 6.8, "genre": "Romance"},
    {"title": "The Last Samurai Returns", "rating": 9.1, "genre": "Action"},
    {"title": "Comedy of Errors", "rating": 7.5, "genre": "Comedy"}
]

df = pd.DataFrame(dummy_movies)
st.dataframe(df)