from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import ollama

from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


app = FastAPI(
    title="langserve",
    description="API for Langchain",
    version="0.1.0",
)



model=ChatOpenAI()

prompt1 = ChatPromptTemplate.from_template(
    "write me a poem about {subject} in 50 words"
)

add_routes(
    app,
    prompt1|model,
    path="/poem",
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

