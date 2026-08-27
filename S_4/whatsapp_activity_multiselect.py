import streamlit as st
import pandas as pd

st.title("WhatsApp Activity Tracker")

# Dummy WhatsApp activity dataset
data = {
    'Day': ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5'],
    'Messages Sent': [120, 150, 90, 200, 180],
    'Photos Shared': [5, 12, 2, 20, 15],
    'Calls Made': [2, 1, 0, 3, 2]
}
df = pd.DataFrame(data).set_index('Day')

selected_columns = st.multiselect(
    "Select activities to visualize:",
    options=df.columns,
    default=['Messages Sent']
)

if selected_columns:
    st.line_chart(df[selected_columns])
else:
    st.info("Please select at least one activity to visualize.")
