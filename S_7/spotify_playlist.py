import streamlit as st
import pandas as pd
from collections import Counter

st.title("My Top 5 Favorite Songs")
st.write("Enter your top 5 favorite songs and their artists:")

artists = []

with st.form("playlist_form"):
    for i in range(1, 6):
        col1, col2 = st.columns(2)
        with col1:
            song = st.text_input(f"Song {i} Name", key=f"song_{i}")
        with col2:
            artist = st.text_input(f"Song {i} Artist", key=f"artist_{i}")
            if artist:
                artists.append(artist.strip())
                
    submit = st.form_submit_button("Analyze Artists")

if submit:
    if len(artists) > 0:
        st.subheader("Artist Appearance Count")
        artist_counts = Counter(artists)
        df = pd.DataFrame.from_dict(artist_counts, orient='index', columns=['Count'])
        st.bar_chart(df)
    else:
        st.warning("Please enter at least one artist to analyze.")
