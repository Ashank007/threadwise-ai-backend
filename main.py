from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from llm_router import generate_reply

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ReplyRequest(BaseModel):
    thread: str
    tone: str
    role: str
    mode: str = "generate"            # generate, analyze, or both

@app.post("/generate-replies")
async def generate_replies(payload: ReplyRequest,x_gemini_api_key: str = Header(None)):
    if not x_gemini_api_key:
        raise HTTPException(status_code=400, detail="Gemini API key is required in header")

    if payload.mode in ["analyze", "both"] and not payload.new_message:
        return {"error": "new_message is required for analyze or both modes"}

    reply = await generate_reply(
        thread=payload.thread,
        role=payload.role,
        tone=payload.tone,
        mode=payload.mode,
        api_key=x_gemini_api_key
    )
    return {"reply": reply}


