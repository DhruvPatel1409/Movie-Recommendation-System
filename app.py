import streamlit as st
import pickle
import pandas as pd
import requests

movies_list = pickle.load(open('C:/Users/ADMIN/Desktop/python jupyter/PROJECTS/MOVIE RECOMMENDATION SYSTEM/movies.pkl','rb'))
similarity = pickle.load(open('C:/Users/ADMIN/Desktop/python jupyter/PROJECTS/MOVIE RECOMMENDATION SYSTEM/similarity.pkl','rb'))
movies_data = movies_list['title'].values

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8b7e3a3a758a697e7a1776ab462392e0&&language=en-US'.format(movie_id))
    data = response.json()
    return  "https://image.tmdb.org/t/p/original/" + data['poster_path']

def recommend(selected_movie):
    movie_index = movies_list[movies_list['title'] == selected_movie].index[0]
    distances = similarity[movie_index, :]
    movies_list_new = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list_new:
        movie_id = movies_list.iloc[i[0]].movie_id
        recommended_movies.append(movies_list.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters

st.title('MOVIE RECOMMENDATION SYSTEM')
selected_movie = st.selectbox(
'Which movie would you like to watch ?',movies_data)

if st.button('Recommend'):
    names,posters = recommend(selected_movie)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])