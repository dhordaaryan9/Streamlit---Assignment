import streamlit as st
import pandas as pd

st.title("Spotify Listening Time")

# Dummy data for Spotify listening time (minutes) for each day of the week
data = {
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    'Minutes': [45, 60, 30, 90, 120, 180, 150]
}
df = pd.DataFrame(data).set_index('Day')

st.area_chart(df)
