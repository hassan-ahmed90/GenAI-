
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
print("Choose the model you want to use:")
print("Press 1 for Sad AI AGENT")
print("Press 2 for Happy AI AGENT")
print("Press 3 for Neutral AI AGENT")
print("Press 4 for Funny AI AGENT")

choice =int(input("Enter your choice: "))
if choice == 1:
    mode="You are my Sad AI Agent, You respond in a sad tone and you are always sad."
elif choice == 2:
    mode="You are my Happy AI Agent, You respond in a happy tone and you are always happy."
elif choice == 3:
    mode="You are my Neutral AI Agent, You respond in a neutral tone and you are always neutral."
elif choice == 4:
    mode="You are my Funny AI Agent, You respond in a funny tone and you are always funny."

message=[
    SystemMessage(content=mode)
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