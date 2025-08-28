from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import os

# Load API key from environment variable (Render -> Environment Variables)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

# Allow frontend domains
origins = [
    "https://safe-space-ai-seven.vercel.app",  # your Vercel frontend
    "http://localhost:3000",                   # local testing
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Hello from backend"}

class ChatRequest(BaseModel):
    messages: list

@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=req.messages
        )
        reply = response.choices[0].message.content

        # Trigger warning detection
        if any(word in reply.lower() for word in ["suicide", "kill", "harm"]):
            reply += "\n\n⚠️ If you're in crisis, please reach out to a local helpline immediately."

        return {"reply": reply}

    except Exception as e:
        # Debugging: show the actual error
        return {"reply": f"Error: {str(e)}"}
