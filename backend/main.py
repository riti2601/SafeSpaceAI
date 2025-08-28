from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware   # ✅ Import this
from pydantic import BaseModel
import openai
import os

# ✅ Use environment variable instead of hardcoding
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# ✅ Add allowed origins (your Vercel frontend + localhost for testing)
origins = [
    "https://safe-space-ai-seven.vercel.app",  # Vercel frontend
    "http://localhost:3000",                   # Local frontend testing
]

# ✅ Add CORS middleware
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
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=req.messages
        )
        reply = response["choices"][0]["message"]["content"]

        # Trigger warning detection
        if any(word in reply.lower() for word in ["suicide", "kill", "harm"]):
            reply += "\n\n⚠️ If you're in crisis, please reach out to a local helpline immediately."

        return {"reply": reply}
    except Exception as e:
        print("Error:", e)  # log the actual error
        return {"reply": "Sorry, I couldn't process your request right now."}
