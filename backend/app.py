from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def home():
    return "Welcome to the home page!"

@app.get("/health")
async def health():
    return {"status": "All is well! Be Happy!"}