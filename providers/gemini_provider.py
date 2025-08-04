import os
import httpx
from dotenv import load_dotenv
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

async def get_gemini_reply(prompt: str,api_key:str) -> str:
    if not api_key:
        raise ValueError("Missing GOOGLE_API_KEY")

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"

    messages = [{"role": "user", "parts": [{"text": prompt}]}]

    body = {
        "contents": messages
    }

    async with httpx.AsyncClient() as client:
        res = await client.post(url, json=body)
        if res.status_code != 200:
            raise Exception(f"Gemini API error: {res.status_code} {res.text}")
        data = res.json()
        return data['candidates'][0]['content']['parts'][0]['text']


