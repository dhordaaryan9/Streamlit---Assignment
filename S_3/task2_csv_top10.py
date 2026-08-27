import streamlit as st
import pandas as pd

st.title("CSV Top 10 Viewer")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.write("### Top 10 Rows")
    st.dataframe(df.head(10))
    
    st.write(f"**Total Rows:** {df.shape[0]}")
    st.write(f"**Total Columns:** {df.shape[1]}")
