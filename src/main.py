# app.py
import json
import streamlit as st
from recommend import df, recommend_movies
from omdb_utils import get_movie_details


config = json.load(open("config.json"))

# OMDB api key
OMDB_API_KEY = config["OMDB_API_KEY"]

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Recommender")
st.markdown(
    """
    <div style='font-size:18px; text-align:justify;'>
        The Movie Recommender App is designed to help users discover films that are similar to the ones they already enjoy. 
        By selecting a movie from the provided list, users can receive a curated set of recommendations based on similarities 
        in genre, storyline, user ratings, or other features defined in the recommendation algorithm. This allows users to 
        easily explore new content without manually searching through large databases or relying on generic suggestions. 
    </div>
    """,
    unsafe_allow_html=True
)

# Using 'title' instead of 'song' now
movie_list = sorted(df['title'].dropna().unique())
selected_movie = st.selectbox("🎬 Select a movie:", movie_list)

if st.button("🚀 Recommend Similar Movies"):
    with st.spinner("Finding similar movies..."):
        recommendations = recommend_movies(selected_movie)
        if recommendations is None or recommendations.empty:
            st.warning("Sorry, no recommendations found.")
        else:
            st.success("Top similar movies:")
            for _, row in recommendations.iterrows():
                movie_title = row['title']
                plot, poster = get_movie_details(movie_title, OMDB_API_KEY)

                with st.container():
                    col1, col2 = st.columns([1, 3])
                    with col1:
                        if poster != "N/A":
                            st.image(poster, width=100)
                        else:
                            st.write("❌ No Poster Found")
                    with col2:
                        st.markdown(f"### {movie_title}")
                        st.markdown(f"*{plot}*" if plot != "N/A" else "_Plot not available_")
