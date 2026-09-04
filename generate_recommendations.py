import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatGroq(
    model_name="openai/gpt-oss-20b",
    temperature=0.2
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a movie recommendation assistant. Given some candidate movies and a user's request, "
                "write a short, natural summary (2-4 sentences) explaining why these movies fit what they're looking for. "
                "Only reference the movies provided below — do not mention any other movies."
                "When referencing the movies have them in this format Series_Title (Released_Year) and don't put quotes around this"),
    ("user", "User request: {query}\n\nCandidate movies:\n{movie_context}")
])

chain = prompt | llm | StrOutputParser()

def generate_recommendations(query, hits):
    movie_context = "\n".join(
        f"- {h.fields['Series_Title']} ({h.fields['Released_Year']}) [{h.fields['Genre']}]: {h.fields['Overview']}"
        for h in hits
    )
    summary = chain.invoke({"query": query, "movie_context": movie_context})
    return summary, hits