import streamlit as st

st.title("Flipkart Product Rating Analyzer")

with st.sidebar:
    st.header("Settings")
    uploaded_file = st.file_uploader("Upload Product CSV", type=["csv"])
    category = st.selectbox("Select Category", ["Electronics", "Fashion", "Home Appliances", "Books"])

st.subheader(f"Analysis Results for {category}")

if uploaded_file:
    st.success("File uploaded successfully! Processing data...")
    # Dummy result output
    st.write("Average Rating: 4.2 / 5.0")
else:
    st.info("Please upload a CSV file in the sidebar to begin analysis.")
