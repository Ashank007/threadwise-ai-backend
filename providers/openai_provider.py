from openai import AsyncOpenAI
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = AsyncOpenAI(api_key=api_key) if api_key else None

async def get_openai_reply(prompt: str) -> str:
    if not client:
        raise RuntimeError("OpenAI API key not set.")

    messages = [
        {"role": "user", "content": prompt}
    ]

    response = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message.content.strip()


