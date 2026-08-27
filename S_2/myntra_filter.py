import streamlit as st

st.title("Myntra Filter Panel")

col1, col2 = st.columns(2)

with col1:
    category = st.selectbox("Category", ['T-Shirts', 'Jeans', 'Shoes'])

with col2:
    max_price = st.number_input("Max Price Range (₹)", min_value=100, value=1000, step=100)

st.markdown("---")
st.subheader("Filter Summary")
st.write(f"**Selected Category:** {category}")
st.write(f"**Budget:** Under ₹{max_price}")
