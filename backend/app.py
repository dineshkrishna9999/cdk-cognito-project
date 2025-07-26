from fastapi import FastAPI, Request
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

@app.get("/")
async def home()->dict:
    return {
        "message": "Welcome to the home page!",
        "config": {
            "A_CONFIG": os.getenv("A_CONFIG","I am default"),
            "A_SECRET": os.getenv("A_SECRET","I am secret")
        }
    }

@app.get("/health")
async def health()->dict:
    return {"status": "All is well! Be Happy!"}