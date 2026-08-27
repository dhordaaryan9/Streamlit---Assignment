import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Daily Social Media Time")

# Dummy data for time spent
data = {
    'App': ['Instagram', 'YouTube', 'WhatsApp'],
    'Time (Hours)': [2.5, 1.5, 1.0]
}
df = pd.DataFrame(data)

fig = px.pie(df, values='Time (Hours)', names='App', title='Time Spent on Social Media')
st.plotly_chart(fig)
