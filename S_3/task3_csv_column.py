import streamlit as st
import pandas as pd

st.title("CSV Column Viewer")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    selected_col = st.selectbox("Select a column to view", df.columns)
    
    st.write(f"### Data for column: {selected_col}")
    st.dataframe(df[[selected_col]])
