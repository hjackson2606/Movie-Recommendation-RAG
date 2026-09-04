from retrieve_movies import retrieve_movies
from generate_recommendations import generate_recommendations

def get_movie_recommendations(query):
    hits = retrieve_movies(query)
    summary, hits = generate_recommendations(query, hits)
    return summary, hits