import os
from dotenv import load_dotenv
from pinecone import Pinecone

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_HOST = os.getenv("PINECONE_INDEX_HOST")

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(host=PINECONE_INDEX_HOST)

def retrieve_movies(query_text):
    results = index.search(
        namespace="movie_list",
        query={
            "inputs": {"text": query_text},
            "top_k": 5
        },
        fields=["Poster_Link", "Series_Title", "Released_Year", "Certificate", "Runtime", "Genre", "Overview"]
    )
    return results["result"]["hits"]