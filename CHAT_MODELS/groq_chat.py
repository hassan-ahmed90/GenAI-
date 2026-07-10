from dotenv import load_dotenv
load_dotenv()
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv()
print(os.getenv("GROQ_API_KEY"))

model = init_chat_model(
    "openai/gpt-oss-120b",
    model_provider="groq"
)
print(model)

response = model.invoke("What is Llama3?")
print(response.content)