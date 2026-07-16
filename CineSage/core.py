from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()
from langchain_mistralai import ChatMistralAI
model= ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.9,
    max_tokens=1000,
)

class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: Optional[str]
    supporting_cast: Optional[List[str]]
    writers: Optional[List[str]]
    producers: Optional[List[str]]
    music_composer: Optional[str]
    cinematographer: Optional[str]
    production_company: Optional[str]
    country: Optional[str]

parser = PydanticOutputParser(pydantic_object=Movie)


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

para=input("Enter the movie paragraph: ")

final_prompt = prompt_template.invoke({
    "paragraph": para
})



response = model.invoke(final_prompt)
movie_data = parser.parse(response.content)
print(movie_data)





