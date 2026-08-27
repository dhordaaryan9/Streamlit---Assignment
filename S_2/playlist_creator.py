import streamlit as st

st.title("Playlist Creator")

with st.sidebar:
    st.header("Create your playlist")
    playlist_name = st.text_input("Playlist Name")
    num_songs = st.number_input("Number of Songs", min_value=1, value=10)
    genre = st.selectbox("Genre", ['Pop', 'Rock', 'Hip-Hop', 'Classical'])
    create_btn = st.button("Create Playlist")

if create_btn:
    st.success("Playlist Created Successfully!")
    st.write(f"**Name:** {playlist_name}")
    st.write(f"**Songs:** {num_songs}")
    st.write(f"**Genre:** {genre}")
