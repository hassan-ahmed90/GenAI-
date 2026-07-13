from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
import os
load_dotenv()

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    # pipeline_kwargs=dict(
    #     max_new_tokens=512,
    #     do_sample=False,
    #     repetition_penalty=1.03,
    # ),
)

chat_model = ChatHuggingFace(llm=llm)

result=chat_model.invoke("What is data engineering?")

print (result.content)