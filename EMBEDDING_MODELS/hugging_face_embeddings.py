from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os
load_dotenv()
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
text=[
    "Hello I'm Hassan Ahmed",
    "I am a data engineer and data scientist",
    "I have experience in building data pipelines and machine learning models"
]
vector = embedding.embed_documents(text)
print(vector)