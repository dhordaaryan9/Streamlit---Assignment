import streamlit as st
import pandas as pd

st.title("Daily Step Count")

# Dummy data for the past 7 days
data = {
    'Days': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    'Steps': [5400, 7200, 4800, 8900, 10200, 12000, 9500]
}
df = pd.DataFrame(data).set_index('Days')

st.line_chart(df)
