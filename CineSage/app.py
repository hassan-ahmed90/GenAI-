import streamlit as st
from movie_extractor import extract_movie

st.set_page_config(
    page_title="🎬 CineSage",
    page_icon="🎬",
    layout="wide",
)

st.title("🎬 CineSage")
st.subheader("Movie Information Extractor using Mistral AI")

paragraph = st.text_area(
    "Enter Movie Paragraph",
    height=250,
    placeholder="Paste the movie description here...",
)

if st.button("Extract Information"):

    if paragraph.strip() == "":
        st.warning("Please enter a movie paragraph.")
    else:

        with st.spinner("Extracting Movie Information..."):

            movie = extract_movie(paragraph)

        st.success("Information Extracted Successfully!")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Basic Information")
            st.write("**Title:**", movie.title)
            st.write("**Release Year:**", movie.release_year)
            st.write("**Director:**", movie.director)
            st.write("**Country:**", movie.country)
            st.write("**IMDb Rating:**", movie.rating)

        with col2:
            st.subheader("Production")
            st.write("**Production Company:**", movie.production_company)
            st.write("**Music Composer:**", movie.music_composer)
            st.write("**Cinematographer:**", movie.cinematographer)

        st.subheader("Genres")
        st.write(movie.genre)

        st.subheader("Cast")
        st.write(movie.cast)

        st.subheader("Supporting Cast")
        st.write(movie.supporting_cast)

        st.subheader("Writers")
        st.write(movie.writers)

        st.subheader("Producers")
        st.write(movie.producers)

        st.subheader("Summary")
        st.info(movie.summary)

        st.subheader("JSON Output")
        st.json(movie.model_dump())