from dotenv import load_dotenv
load_dotenv()
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv()
print(os.getenv("MISTRAL_API_KEY"))

model = init_chat_model(
    "mistral-large-latest",
    model_provider="mistralai",
    temperature=0,
    max_tokens=1000
)
# print(model)

response = model.invoke("Write a poem on AI?")
print(response.content)