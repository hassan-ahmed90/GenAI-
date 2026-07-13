
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import os

load_dotenv()
print(os.getenv("MISTRAL_API_KEY"))

model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.9,
    max_tokens=1000,
)
message=[
    SystemMessage(content="You are my AI/ML Teacher."),
]
print("Type '0' to quit the chat.")
while True:
    
    prompt= input("YOU :")
    message.append(HumanMessage(content=prompt))
    if prompt == "0":
        break
    response = model.invoke(message)
    message.append(AIMessage(content=response.content))
    print("BOT: ",response.content)