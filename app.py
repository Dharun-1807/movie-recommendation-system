import streamlit as st
import pickle
import requests

# Load data FAST (no recomputation)
movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

# Recommendation function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]

    distances = similarity[index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended = []
    for i in movies_list:
        recommended.append(movies.iloc[i[0]].title)

    return recommended


# UI
st.set_page_config(page_title="Movie Recommender")

import requests

def fetch_poster(movie_title):
    api_key = "YOUR_API_KEY"

    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_title}"

    response = requests.get(url)
    data = response.json()

    try:
        poster_path = data['results'][0]['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500" + poster_path
        return full_path
    except:
        return None
st.title("🎬 Movie Recommendation System")

selected_movie = st.selectbox(
    "Select a movie",
    movies['title'].values
)

if st.button("Recommend"):
    results = recommend(selected_movie)

    st.subheader("🎯 Top Recommended Movies")

    for i, movie in enumerate(results, 1):
        st.markdown(f"**{i}. 🎬 {movie}**")