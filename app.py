import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.title("Movie Recommendation system")
movie_df = pickle.load(open("movie_recm.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))
list_movie = np.array(movie_df["title"])
option = st.selectbox("Select Movie", (list_movie))

def movie_recommend(movie):
    index = movie_df[movie_df['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommendations = []
    for i in distances[1:6]:
        recommended_movie_title = movie_df.iloc[i[0]].title
        similarity_score = i[1]
        recommendations.append((recommended_movie_title, similarity_score))
    return recommendations

if st.button('Recommend Me'):
    st.write('Movies Recommended for you are:')
    recommendations = movie_recommend(option)
    df = pd.DataFrame({
        'Recommended Movie': [rec[0] for rec in recommendations],
        'Similarity Score': [rec[1] for rec in recommendations]
    })
    st.table(df)
