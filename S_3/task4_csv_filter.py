import streamlit as st
import pandas as pd

st.title("CSV Global Filter")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    search_term = st.text_input("Search term (case-insensitive)")
    
    if search_term:
        mask = df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)
        filtered_df = df[mask]
        st.write(f"### Search Results ({len(filtered_df)} rows found)")
        st.dataframe(filtered_df)
    else:
        st.write("### Full Data")
        st.dataframe(df)
