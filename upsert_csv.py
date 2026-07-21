import os
from dotenv import load_dotenv
from pinecone import Pinecone
import pandas as pd

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_HOST = os.getenv("PINECONE_INDEX_HOST")

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(host=PINECONE_INDEX_HOST)
df = pd.read_csv("imdb_top_1000.csv")

movies = []
for i, row in df.iterrows():
    movie_info = {
        "_id": str(i),
        "Poster_Link": row["Poster_Link"],
        "Series_Title": row["Series_Title"],
        "Released_Year": row["Released_Year"],
        "Certificate": row["Certificate"],
        "Runtime": row["Runtime"],
        "Overview": row["Overview"],
    }
    movies.append(movie_info)

def chunks(movies, batch_size=96):
    for i in range(0, len(movies), batch_size):
        yield movies[i:i+batch_size]

for batch in chunks(movies, batch_size=96):
    index.upsert_records(namespace="movie_list", records=batch)