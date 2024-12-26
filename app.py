import pickle
import streamlit as st
import requests
import gzip


# Function to fetch movie poster
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()

        if 'poster_path' in data and data['poster_path']:
            poster_path = data['poster_path']
            full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
            return full_path
        else:
            return None  # In case no poster is found

    except Exception as e:
        print(f"Error fetching poster for movie ID {movie_id}: {e}")
        return None


# Function to get movie recommendations
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:  # Fetch top 5 recommendations (skip the first one, which is the selected movie)
        movie_id = movies.iloc[i[0]].movie_id
        poster_url = fetch_poster(movie_id)

        recommended_movie_posters.append(
            poster_url if poster_url else "https://via.placeholder.com/500x750?text=No+Poster")
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters


# Streamlit interface
st.header('Movie Recommender System')

# Load movies and similarity data (make sure to use the correct paths)
movies = pickle.load(open('movie_list.pkl', 'rb'))

# Open and load the compressed pickle file
with gzip.open('similarity.pkl.gz', 'rb') as f:
    similarity = pickle.load(f)


# Create a movie selection dropdown
movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

# When the button is clicked, show recommendations
if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    # Create columns to display recommended movies and their posters
    cols = st.columns(5)  # Create 5 columns

    for idx, col in enumerate(cols):
        with col:
            st.text(recommended_movie_names[idx])
            st.image(recommended_movie_posters[idx])
