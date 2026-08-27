import streamlit as st

st.title("Instagram Like Counter")

if 'likes' not in st.session_state:
    st.session_state.likes = 0

if st.button("❤️ Like"):
    st.session_state.likes += 1

st.write(f"**Likes:** {st.session_state.likes}")
