from fastapi import FastAPI
from pydantic import BaseModel
import openai

openai.api_key = "YOUR_OPENAI_KEY"  # Replace with environment variable

app = FastAPI()

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
        return {"reply": "Sorry, I couldn't process your request right now."}
