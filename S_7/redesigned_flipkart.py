import streamlit as st

st.set_page_config(layout="wide")
st.title("Redesigned Flipkart Rating Analyzer")

# Task 4: Using st.columns to arrange input and output side by side
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Configuration")
    uploaded_file = st.file_uploader("Upload Product CSV", type=["csv"])
    category = st.selectbox("Select Category", ["Electronics", "Fashion", "Home Appliances", "Books"])
    
    # Task 4: Using st.expander to hide advanced options
    with st.expander("Advanced Options"):
        min_reviews = st.slider("Minimum Reviews Count", 0, 1000, 50)
        exclude_outofstock = st.checkbox("Exclude Out of Stock Items", value=True)

with col2:
    st.subheader("Results Dashboard")
    if uploaded_file:
        st.success(f"Displaying analytics for {category}...")
        st.metric(label="Average Rating", value="4.5", delta="0.2")
        st.write(f"Filters applied: Min Reviews={min_reviews}, Exclude OOS={exclude_outofstock}")
    else:
        st.info("Upload data in the configuration panel on the left to view the dashboard.")
