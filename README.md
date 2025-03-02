# Movie Recommendation System Using Cosine Similarity

This project implements a movie recommendation system based on **Cosine Similarity**. It uses user ratings and movie features to recommend movies that are similar to those a user has already watched or liked. The system leverages a **content-based filtering** approach, where similarity between movies is calculated using the cosine similarity metric.

## Project Overview

The goal of this project is to build a recommendation system that can suggest movies to users based on the similarity between movies. By analyzing the features of movies (such as genre, director, and cast) and/or user ratings, the system can recommend movies that are most similar to a user's past preferences. This approach uses **Cosine Similarity** to measure how similar movies are to each other.

## Technologies Used

- **Python**: The primary programming language used.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical operations.
- **Scikit-learn**: For calculating cosine similarity and other machine learning tasks.
- **Streamlit** (optional): If you choose to deploy the recommendation system as a web application.
- **Jupyter Notebook**: For developing and testing the system (optional).

## Dataset

The dataset used for this project is the [MovieLens dataset](https://grouplens.org/datasets/movielens/), which contains movie ratings and metadata (such as movie titles, genres, and tags). The data includes:
- **Movie Data**: Movie titles, genres, release year, etc.
- **Genres**: Type of each movie.
- **Tags**: User-generated tags for movies.

Feel free to use your own dataset or download the one provided.

## Installation

To run the project, follow these steps:

### 1. Clone the repository
```bash
https://github.com/Maddy10/Movie-Recommender-System.git
cd movie-recommendation-system
