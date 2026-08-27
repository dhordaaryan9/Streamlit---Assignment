import streamlit as st
import pandas as pd

st.title("Food Delivery Orders")

# Dummy data for Zomato, Swiggy, Domino's over the last month
data = {
    'Platform': ['Zomato', 'Swiggy', "Domino's"],
    'Orders': [15, 12, 5]
}
df = pd.DataFrame(data).set_index('Platform')

st.bar_chart(df)
