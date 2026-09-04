import streamlit as st
import requests

st.set_page_config(
    page_title="Movie Recommendation App",
    page_icon="🎬",
    layout="wide",
)

st.title("🎬 Welcome to Movie Recommendation App")

query = st.text_input("What are you in the mood to watch?")

if st.button("Recommend Me"):
    payload = {
        "query": query
    }

    response = requests.post("http://127.0.0.1:8000/recommend-movies", json=payload)

    if response.status_code == 200:
        result = response.json()

        st.write(result["summary"])
        
        col1, col2, col3, col4, col5 = st.columns(5)
        movie1, movie2, movie3, movie4, movie5 = result["hits"][0], result["hits"][1], result["hits"][2], result["hits"][3], result["hits"][4]

        with col1:
            st.header(f"{movie1['Series_Title']} ({movie1['Released_Year']})")
            st.image(movie1["Poster_Link"])
            st.caption(f"{movie1['Genre']} • {movie1['Certificate']} • {movie1['Runtime']}")
            st.write(movie1["Overview"])

        with col2:
            st.header(f"{movie2['Series_Title']} ({movie2['Released_Year']})")
            st.image(movie2["Poster_Link"])
            st.caption(f"{movie2['Genre']} • {movie2['Certificate']} • {movie2['Runtime']}")
            st.write(movie2["Overview"])

        with col3:
            st.header(f"{movie3['Series_Title']} ({movie3['Released_Year']})")
            st.image(movie3["Poster_Link"])
            st.caption(f"{movie3['Genre']} • {movie3['Certificate']} • {movie3['Runtime']}")
            st.write(movie3["Overview"])

        with col4:
            st.header(f"{movie4['Series_Title']} ({movie4['Released_Year']})")
            st.image(movie4["Poster_Link"])
            st.caption(f"{movie4['Genre']} • {movie4['Certificate']} • {movie4['Runtime']}")
            st.write(movie4["Overview"])

        with col5:
            st.header(f"{movie5['Series_Title']} ({movie5['Released_Year']})")
            st.image(movie5["Poster_Link"])
            st.caption(f"{movie5['Genre']} • {movie5['Certificate']} • {movie5['Runtime']}")
            st.write(movie5["Overview"])
