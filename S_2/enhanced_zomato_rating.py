import streamlit as st

st.title("Enhanced Zomato Order Rating")

with st.sidebar:
    st.header("Feedback Form")
    rating = st.slider("Rate your last order (Stars)", 1, 5, 5)
    food_type = st.radio("Food Type", ['Veg', 'Non-Veg'])
    submit_btn = st.button("Submit Feedback")

if submit_btn:
    st.success("Thank you for your feedback!")
    st.write(f"You rated your **{food_type}** order with **{rating} stars**.")
