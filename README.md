# Movie Recommendation RAG
🔗 **[Try the live app](https://movie-recommendation-rag-hj.streamlit.app)** | **[API docs](https://movie-recommendation-rag-pjc9.onrender.com/docs)**

> Note: the API is hosted on a free tier that spins down after inactivity — the first request may take 30–60 seconds while it wakes up.

## About Dataset
- IMDB Top 1000 movies and TV shows
- Includes title, release year, certificate, runtime, genre, IMDB rating, overview, and poster link
- 101 rows had a missing `Certificate` value, standardized to `"Not Rated"` after individually verifying all 101 proved unreliable — even reputable sources disagree on the correct classification for older, pre-1968 films

## Pipeline Overview
The RAG pipeline includes:
- Ingestion: movie metadata is cleaned and upserted into a Pinecone vector index, with each movie's `Overview` embedded via Pinecone's hosted `llama-text-embed-v2` model (integrated embedding — no local embedding model or GPU required)
- Retrieval: a user's query is embedded and compared against the stored vectors using semantic similarity search, returning the top 5 most relevant movies
- Generation: the retrieved movies and the user's query are passed to `openai/gpt-oss-20b` (via LangChain and Groq), which writes a short natural-language summary explaining why these specific movies fit — strictly grounded in the retrieved candidates
- Retrieval and generation are implemented as independent, separately testable functions, tied together by a single orchestration layer

## Project Structure
```
├── ingest.py                    # One-time script: loads CSV, upserts records into Pinecone
├── retrieve_movies.py           # Semantic search against the Pinecone index
├── generate_recommendations.py  # LangChain + Groq prompt chain
├── pipeline.py                  # Orchestrates retrieval → generation
├── main.py                      # FastAPI app and endpoint
├── streamlit_app.py             # Frontend
└── imdb_top_1000.csv            # Source dataset
```

## Deployment
The pipeline is served via a **FastAPI** REST API (hosted on Render) and accessed through a **Streamlit** front-end (hosted on Streamlit Community Cloud). The interface lets a user describe what they're in the mood to watch and receive a generated recommendation summary alongside five matching movies, each with poster, genre, certificate, runtime, and overview.
