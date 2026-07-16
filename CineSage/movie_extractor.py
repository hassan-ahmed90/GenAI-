from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_mistralai import ChatMistralAI
from pydantic import BaseModel
from typing import List, Optional

load_dotenv()

model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0,
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
Extract Movie Information from the given paragraph.

{format_instructions}
""",
        ),
        ("human", "{paragraph}"),
    ]
)


def extract_movie(paragraph):
    chain = prompt_template | model | parser

    return chain.invoke(
        {
            "paragraph": paragraph,
            "format_instructions": parser.get_format_instructions(),
        }
    )