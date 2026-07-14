import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

# Load environment variables
load_dotenv()

# Initialize model
model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.9,
    max_tokens=1000,
)

# Prompt Template
prompt_template = ChatPromptTemplate.from_messages(
[
(
"system",
"""
You are CineSage, an expert Movie Information Extraction Assistant.

Your responsibility is to analyze an unstructured movie paragraph and extract the most useful information in a clean, structured format.

Guidelines:
- Read the paragraph carefully.
- Extract only information that is explicitly mentioned.
- Do not invent or assume missing information.
- If a piece of information is unavailable, write "Not Mentioned".
- Keep the generated summary concise (2–3 sentences).
- Return only the extracted information.
- Do not include explanations or additional commentary.

Extract the following information:

Movie Title
Release Year
Genre
Director
Main Cast
Supporting Cast
Writers
Producers
Music Composer
Cinematographer
Production Company
Country
Language
Runtime
IMDb Rating
Rotten Tomatoes Rating
Box Office
Awards
Setting / Location
Main Characters
Plot
Main Theme
Keywords
Notable Features
Quick Summary

Present the information in a clean and readable format.
"""
),
(
"human",
"""
Movie Paragraph:

{paragraph}
"""
)
]
)

# ---------------------- UI ----------------------

st.set_page_config(
    page_title="CineSage",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 CineSage")
st.write("Extract structured movie information from a raw movie paragraph.")

para = st.text_area(
    "Enter Movie Paragraph",
    height=250,
    placeholder="Paste your movie paragraph here..."
)

if st.button("Extract Information", use_container_width=True):

    if para.strip() == "":
        st.warning("Please enter a movie paragraph.")
    else:
        with st.spinner("Analyzing movie paragraph..."):

            final_prompt = prompt_template.invoke({
                "paragraph": para
            })

            response = model.invoke(final_prompt)

        st.subheader("📋 Extracted Information")
        st.text(response.content)