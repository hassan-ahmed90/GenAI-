from dotenv import load_dotenv
load_dotenv()
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv()
print(os.getenv("GEMINI_API_KEY"))

model = init_chat_model(
    "gemini-2.5-flash",
    model_provider="google_genai"
)

print(model)

response = model.invoke("What is Cricket?")
print(response.content)