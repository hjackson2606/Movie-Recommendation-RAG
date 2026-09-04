from fastapi import FastAPI
from pydantic import BaseModel
from pipeline import get_movie_recommendations

app = FastAPI()

class RecommendRequest(BaseModel):
    query: str

@app.post("/recommend-movies")
def recommend_movies(request: RecommendRequest):
    summary, hits = get_movie_recommendations(request.query)
    return {
        "summary": summary, 
        "hits": [h.fields for h in hits]
    }