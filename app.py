import pickle
import streamlit as st
import requests



st.header("Movie Recommendation System")
movies = pickle.load(open(r"Artifacts/movie_list.pkl","rb"))
similarity = pickle.load(open(r"Artifacts/similarity.pkl","rb"))

api_key = 'YOUR OMDB API KEY'
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=ded9a698ff167d9046b56bd09f2d806c&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['original_title']==movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])
    recommended_movie_name = []
    movie_poster = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].id
        movie_poster.append(fetch_poster(movie_id))
        recommended_movie_name.append(movies.iloc[i[0]].original_title)
    return recommended_movie_name,movie_poster




movie_list = movies['original_title'].values
selected_movie = st.selectbox(
    'Type or Select a movie to get recommendation',
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
