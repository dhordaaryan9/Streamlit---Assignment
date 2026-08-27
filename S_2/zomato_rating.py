import streamlit as st

st.title("Zomato Order Rating")

rating = st.slider("Rate your last order (Stars)", 1, 5, 5)
food_type = st.radio("Food Type", ['Veg', 'Non-Veg'])

if st.button("Submit Feedback"):
    st.success("Thank you for your feedback!")
    st.write(f"You rated your **{food_type}** order with **{rating} stars**.")
