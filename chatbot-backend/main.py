# # main.py
# import warnings
# warnings.filterwarnings("ignore", message="The `dict` method is deprecated; use `model_dump` instead.")
# warnings.filterwarnings("ignore", category=UserWarning)

# import os
# import glob

# from tqdm import tqdm
# from dotenv import load_dotenv
# from openai import OpenAI
# from typing import List
# from ddgs import DDGS
# # from sentence_transformers import SentenceTransformer

# from langchain import hub

# from langchain_core.documents import Document
# from langchain.document_loaders import PyPDFLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.embeddings.base import Embeddings
# from langchain.vectorstores import FAISS

# from langchain.chains import RetrievalQA
# from langchain.chains import LLMMathChain

# from langchain.chat_models import ChatOpenAI
# from langchain.chat_models import AzureChatOpenAI

# from langchain.tools import StructuredTool
# from langchain.tools import DuckDuckGoSearchRun
# from langchain.memory import ConversationBufferMemory
# from langchain.schema import HumanMessage, SystemMessage
# from langchain.callbacks.base import BaseCallbackHandler

# from langchain.agents import AgentExecutor, AgentType, Tool
# from langchain.agents import create_react_agent, initialize_agent, load_tools
# # from langchain.agents.agent_types import AgentType

# from langchain.tools.retriever import create_retriever_tool


import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

##############################################################################
# Load environment variables from the .env file
##############################################################################
load_dotenv()

endpoint = os.getenv("ENDPOINT")
api_key = os.getenv("API_KEY")

llm_name = "gpt-4o"  # Azure deployment name (not model name)
embedding_name = 'text-embedding-3-large'

##############################################################################
# --- 1. Initialize FastAPI and OpenAI Client ---
##############################################################################
app = FastAPI()
client = OpenAI(
    api_key=api_key,  
    base_url=f"{endpoint}/openai/v1/",
    )

# --- 2. Configure CORS ---
# This is crucial for allowing your React frontend to communicate with this backend.
# It's a security feature that browsers enforce.
origins = [
    "http://localhost:5173",  # Default Vite React dev server
    "http://localhost:3000",  # Common Create React App dev server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Allow all methods (GET, POST, etc.)
    allow_headers=["*"], # Allow all headers
)

# --- 3. Define the Request Data Structure ---
# Pydantic model ensures the incoming data has the correct format.
class ChatInput(BaseModel):
    user_message: str

# --- 4. Create API Endpoints ---
@app.get("/")
async def health_check():
    """A simple endpoint to confirm the server is running."""
    return {"status": "ok"}

@app.post("/chat")
async def chat_with_ai(input_data: ChatInput):
    """The main endpoint to handle chat interactions."""
    
    context_prompt = (
        "You are a Healthcare AI agent called Magnol.AI ChatBot "
        "You are created by Eli Lilly Digital Health "
        "You are strictly not allowed to answer any questions outside of the Healthcare domain "
        "If asked, reply: I am Magnol.AI ChatBot, I cannot provide assistance on topics outside the healthcare domain. "
        "You are allowed to answer that you are created by Eli Lilly Digital Health "
        "Keep response short and sweet, ideally under 150 words. "
        )
    
    try:
        # Forward the user's message to the OpenAI API
        completion = client.chat.completions.create(
            model=llm_name, # Replace with your model deployment name.
            messages=[
                {"role": "system", "content": context_prompt},
                {"role": "user", "content": input_data.user_message}
            ]
        )
        # Extract and return the AI's response
        bot_response = completion.choices[0].message.content
        return {"bot_response": bot_response}

    except Exception as e:        
        print(e)
        # Properly handle potential API errors
        raise HTTPException(status_code=500, detail=str(e))
        # return {"bot_response": e}