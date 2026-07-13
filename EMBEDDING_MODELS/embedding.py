from langchain_openai import ChatOpenAIEmbeddings

embeddings = ChatOpenAIEmbeddings(
    model="text-embedding-3-large",
    dimension=64,
)
text=[
    "Hello I'm Hassan Ahmed",
    "I am a data engineer and data scientist",
    "I have experience in building data pipelines and machine learning models"
]
vector = embeddings.embed_query(text) 
print(vector)