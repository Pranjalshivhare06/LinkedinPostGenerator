from dotenv import load_dotenv
from langchain_groq import ChatGroq 
import os 
import sys

sys.stdout.reconfigure(encoding="utf-8")
load_dotenv()

llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="openai/gpt-oss-20b")

if __name__ == "__main__":
    response = llm.invoke("what is color of sky and earth?")
    print(response.content)