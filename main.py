from langchain.llms import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()


api_key = os.environ.get("OPENAI_API_KEY")

llm = OpenAI(openai_api_key=api_key)

result = llm("Write a short poem")
print(result)
